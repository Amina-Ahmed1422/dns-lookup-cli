import argparse
import dns.resolver

print("DNS TOOL STARTED")


def lookup_dns(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)

        print(f"\n{record_type} Records:")
        for answer in answers:
            print(f"  {answer}")

    except dns.resolver.NoAnswer:
        print(f"\n{record_type} Records:")
        print("  No record found.")

    except dns.resolver.NXDOMAIN:
        print(f"\nDomain does not exist: {domain}")

    except Exception as e:
        print(f"\nError: {e}")


parser = argparse.ArgumentParser( 
    description="Simple DNS Lookup CLI Tool" 
)
parser.add_argument(
     "domain", 
     help="Domain name to investigate"
)
args = parser.parse_args()
domain = args.domain

print("=" * 40)
print("       DNS Lookup CLI Tool")
print("=" * 40) 
print(f"Domain: {domain}")

for record_type in ["A", "AAAA", "MX", "NS", "CNAME"]:
    lookup_dns(domain, record_type)