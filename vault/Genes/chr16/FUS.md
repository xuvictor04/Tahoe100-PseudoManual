---
symbol: "FUS"
type: "gene"
col: 1582
ensembl_id: "ENSG00000089280"
name: "FUS DNA/RNA binding protein"
location: "16p11.2"
module: 93
arm: "+"
pooled_cpm: 252.15
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/093", "written"]
generated_by: "tahoemap"
---

# FUS

*FUS DNA/RNA binding protein* — 16p11.2

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> FUS is an abundant, essential RNA- and DNA-binding protein involved in transcription, splicing and the DNA damage response, mutated in familial ALS and rearranged in several sarcomas — and the highly expressed gene lying 17.05 kb 5′ of [[TRIM72]] on the same strand, so transcription running past it can be counted as TRIM72 mRNA ([[Readthrough spillover]]).

## What it is

FUS (fused in sarcoma, also TLS) is a member of the FET family alongside EWSR1 and TAF15. Its architecture is a list of interaction modules rather than an enzyme: an N-terminal QGSY-rich low-complexity prion-like domain, RGG repeats, an RRM, a zinc finger, and a C-terminal PY-type nuclear localisation signal read by Transportin-1/karyopherin-β2. It is predominantly nuclear but shuttles, and binds thousands of transcripts with loose specificity. Functionally it has been placed at transcription — interacting with the RNA polymerase II C-terminal domain and affecting initiation and elongation — at alternative splicing, at mRNA transport, and in paraspeckles with NEAT1. It also participates in the DNA damage response, recruited rapidly to damage sites in a PARP- and poly(ADP-ribose)-dependent manner, with reported roles in double-strand break repair and in ligation during oxidative damage repair.

The low-complexity domain makes FUS a phase-separating protein, and the property that lets it condense functionally lets it solidify pathologically: purified FUS undergoes a liquid-to-solid transition that disease mutations accelerate. Clinically it is known from two directions. Mutations cause ALS type 6 and some frontotemporal dementia; most cluster in the PY-NLS, weaken Transportin binding, and drive cytoplasmic mislocalisation and inclusion formation, so the disease is usually read as mislocalisation rather than simple loss of function. Separately, translocations fuse the FUS N-terminal low-complexity domain to DNA-binding partners — FUS–DDIT3 (CHOP) in myxoid liposarcoma, FUS–ERG in leukaemia, FUS–CREB3L2 in low-grade fibromyxoid sarcoma — where it acts as a potent transactivation module. FUS is highly expressed in essentially all proliferating cells.

## What is uncertain

Whether FUS is a quantitatively sufficient donor is not established. In the earlier MG53/p53 study, the strand-aware evidence that plus-strand readthrough is really occurring at this locus is solid, but the flux arithmetic calibrated on it over-predicts the observed rise, so "FUS readthrough explains the MG53 signal" overstates what has been shown — the honest form is that it is the leading account and the numbers do not yet close. Whether changes in FUS's own counts are pathway responses is also unsettled: FUS is not a known p53 target and has no established p53 response element, so movement in it more plausibly tracks global transcriptional output or termination fidelity than any specific signal. And nothing about FUS's protein-level biology — condensation state, localisation, DDR recruitment — is visible in mRNA, so a change in FUS counts says nothing about whether FUS is functioning normally in these cells.

## References

- Crozat et al., 1993, Nature — identified FUS/TLS through its fusion to CHOP in human myxoid liposarcoma.
- Kwiatkowski et al., 2009, Science — found mutations in FUS/TLS on chromosome 16 causing familial amyotrophic lateral sclerosis.
- Vance et al., 2009, Science — independently identified FUS mutations as the cause of familial ALS type 6.
- Patel et al., 2015, Cell — showed a liquid-to-solid phase transition of FUS that is accelerated by disease mutation.
- Mastrocola et al., 2013, Journal of Biological Chemistry — showed FUS acts downstream of PARP in the response to DNA damage, with recruitment dependent on poly(ADP-ribose).

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.19× (z +18.2, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.761× (z -4.3, q 0.009, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBMX]] (+0.58, fdr 1e-05), [[TEX14]] (+0.57, fdr 1e-05), [[POLR2A]] (+0.54, fdr 1e-04); moves opposite to [[PEX2]] (-0.53, fdr 3e-05), [[RBIS]] (-0.52, fdr 3e-05), [[LYPLAL1]] (-0.51, fdr 4e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1582.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.19×** | +18.2 | 0e+00 | 42/48 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +12.6 | 8e-34 | 42/49 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.04×** | +11.3 | 4e-27 | 48/48 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.68×** | +8.5 | 3e-15 | 43/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.67×** | +8.4 | 5e-15 | 39/48 (NCI-H460, PANC-1, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +7.0 | 2e-10 | 40/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +6.9 | 4e-10 | 37/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +6.6 | 4e-09 | 43/50 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.05×** | +6.2 | 5e-08 | 44/48 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.8 | 4e-07 | 43/48 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.43×** | +5.7 | 6e-07 | 35/47 (SHP-77, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.90×** | +5.5 | 2e-06 | 42/49 (AsPC-1, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +4.5 | 2e-04 | 33/47 (HT-29, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.31×** | +4.5 | 3e-04 | 29/48 (SW480, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.35×** | +4.4 | 4e-04 | 35/48 (NCI-H460, PANC-1, …) | rises with dose | position effect removed |
| [[Diphenhydramine (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.051 | 22/48 (MIA PaCa-2, Panc 03.27, …) | top dose only |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.051 | 26/48 (COLO 205, J82, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.056 | 16/48 (MIA PaCa-2, Hs 766T, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.058 | 6/49 (Panc 03.27, LoVo, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.058 | 22/47 (SW48, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1582.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.761×** | -4.3 | 0.009 | 35/47 (NCI-H1573, C-33 A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.786×** | -4.0 | 0.021 | 33/48 (J82, RKO, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.876× | -3.1 | 0.38 | 11/48 (RKO, A-172, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.833× | -3.0 | 0.38 | 23/47 (H4, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1582. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 212 | 16 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +21.7) | — |
| [[PANC-1 (line)]] | alt | 242 | 9 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +16.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.31× (z +16.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 300 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.4) | — |
| [[LOX-IMVI (line)]] | wt | 253 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +14.0) | — |
| [[NCI-H1792 (line)]] | alt | 161 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +19.0) | — |
| [[AsPC-1 (line)]] | alt | 279 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +25.2) | — |
| [[LS 180 (line)]] | wt | 186 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +16.7) | — |
| [[SW480 (line)]] | alt | 220 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +13.0) | — |
| [[A549 (line)]] | wt | 218 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +16.7) | — |
| [[KATO III (line)]] | alt | 189 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.16× (z +17.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.22× (z +14.0) | — |
| [[NCI-H1573 (line)]] | alt | 267 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +17.1) | — |
| [[SW 900 (line)]] | alt | 212 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.9) | — |
| [[SW1417 (line)]] | alt | 262 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +16.1) | — |
| [[BT-474 (line)]] | alt | 247 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.62× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 249 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +15.8) | — |
| [[LoVo (line)]] | wt | 249 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +15.1) | — |
| [[A498 (line)]] | wt | 372 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +22.6) | — |
| [[COLO 205 (line)]] | alt | 214 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +18.1) | — |
| [[HepG2_C3A (line)]] | wt | 282 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.13× (z +8.8) ⚠ toxic; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 251 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +12.5) | — |
| [[HT-29 (line)]] | alt | 183 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +14.0) | — |
| [[J82 (line)]] | alt | 315 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 226 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +14.0) | — |
| [[SK-MEL-2 (line)]] | alt | 252 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.6) | — |
| [[SW48 (line)]] | wt | 260 | 3 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.54× (z +10.1) | — |
| [[A-172 (line)]] | wt | 258 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +11.0) | — |
| [[C32 (line)]] | wt | 282 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +15.5) | — |
| [[H4 (line)]] | wt | 274 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +10.1) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[Hs 766T (line)]] | wt | 193 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +12.8) | — |
| [[HS-578T (line)]] | alt | 177 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +12.7) | — |
| [[hTERT-HPNE (line)]] | wt | 290 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +14.9) | — |
| [[Panc 03.27 (line)]] | alt | 181 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +12.5) | — |
| [[RKO (line)]] | wt | 286 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 312 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.39× (z +10.8) ⚠ toxic; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.77× (z +10.3) | — |
| [[A-427 (line)]] | wt | 318 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 272 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +13.6) | — |
| [[HCT15 (line)]] | alt | 309 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 320 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +9.6) | — |
| [[NCI-H2347 (line)]] | alt | 169 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +13.1) | — |
| [[SNU-1 (line)]] | wt | 274 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.30× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 250 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +11.2) | — |
| [[SW 1271 (line)]] | alt | 340 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 304 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 315 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 220 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 358 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 258 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 284 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 387 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1582), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBMX]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 900 |
| [[TEX14]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[POLR2A]] | +0.54 | +0.52 / +0.34 | both halves | 1e-04 | pathway: Dengue Virus-Host Interactions; STRING 520 |
| [[PTBP1]] | +0.52 | +0.50 / +0.54 | both halves | 1e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 852 |
| [[NASP]] | +0.52 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[SRSF7]] | +0.52 | +0.65 / +0.44 | both halves | 3e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 686 |
| [[TRPV1]] | +0.52 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[LINC00910]] | +0.51 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[WDR74]] | +0.51 | +0.54 / +0.36 | both halves | 1e-04 |  |
| [[KLHL15]] | +0.51 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[MEPCE]] | +0.51 | +0.48 / +0.34 | both halves | 1e-04 | STRING 452 |
| [[NXF1]] | +0.50 | +0.54 / +0.39 | both halves | 5e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 493 |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX2]] | -0.53 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[RBIS]] | -0.52 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[LYPLAL1]] | -0.51 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[SERAC1]] | -0.49 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[MAPRE3]] | -0.48 | -0.49 / -0.29 | both halves | 2e-04 |  |
| [[MFSD9]] | -0.48 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[BLVRA]] | -0.48 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[TTC1]] | -0.46 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[USP30]] | -0.46 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[PSMG2]] | -0.46 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[MOSPD2]] | -0.45 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[CCNC]] | -0.45 | -0.38 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.482). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (27.9, -26.1); signed map (5.0, 16.3). **Vector** length 111, 39.8% of its response variance represented; |z| ≥ 3 in 1,076 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +6.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +5.8 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +12.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +3.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +3.4 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +1.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.7 | +0.7 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.7 | -1.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.2 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -1.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.8 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.6 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.4 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.0 | -0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | +1.3 |

## What is on record

|  |  |
|---|---|
| Name | FUS DNA/RNA binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:31,180,138-31,196,963 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TLS, FUS1, hnRNP-P2, HNRNPP2; previously ALS6 |
| Gene groups (HGNC) | Zinc fingers RANBP2-type; RNA binding motif containing; Heterogeneous nuclear ribonucleoproteins; FET protein family |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 9 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P35637](https://www.uniprot.org/uniprotkb/P35637) (RNA-binding protein FUS):

> DNA/RNA-binding protein that plays a role in various cellular processes such as transcription regulation, RNA splicing, RNA transport, DNA repair and damage response. Binds to ssRNA containing the consensus sequence 5'-AGGUAA-3'. Binds to nascent pre-mRNAs and acts as a molecular mediator between RNA polymerase II and U1 small nuclear ribonucleoprotein thereby coupling transcription and splicing. Also binds its own pre-mRNA and autoregulates its expression; this autoregulation mechanism is …

**Summary**, from NCBI Gene [2521](https://www.ncbi.nlm.nih.gov/gene/2521):

> This gene encodes a multifunctional protein component of the heterogeneous nuclear ribonucleoprotein (hnRNP) complex. The hnRNP complex is involved in pre-mRNA splicing and the export of fully processed mRNA to the cytoplasm. This protein belongs to the FET family of RNA-binding proteins which have been implicated in cellular processes that include regulation of gene expression, maintenance of genomic integrity and mRNA/microRNA processing. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:4010](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4010) · Entrez [2521](https://www.ncbi.nlm.nih.gov/gene/2521) · UniProt [P35637](https://www.uniprot.org/uniprotkb/P35637) · Ensembl [ENSG00000089280](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089280)

## Data

Gene col 1582: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1582); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1582, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1582]; `tensor/DDL_lfc|DDL_z.npy` [1582]; `embed/gene_vectors.npy` [1582]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1582 or target_col == 1582). Every well: [[FUS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/FUS.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
