---
symbol: "XPC"
type: "gene"
col: 7837
ensembl_id: "ENSG00000154767"
name: "XPC complex subunit, DNA damage recognition and repair factor"
location: "3p25.1"
module: 62
arm: "+"
pooled_cpm: 65.11
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 11
n_dd_up_clean: 25
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# XPC

*XPC complex subunit, DNA damage recognition and repair factor* — 3p25.1

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> XPC is the sensor that finds bulky DNA lesions anywhere in the genome and starts nucleotide-excision repair there, and it is one of the repair genes p53 induces.

## What it is

Nucleotide-excision repair comes in two flavours that differ only in how the lesion is found. In transcription-coupled repair, a stalled RNA polymerase is the detector. In global-genome repair — the rest of the genome, including the strand nobody is transcribing — the detector is XPC, working as a heterotrimer with RAD23B and centrin-2. XPC does not read the lesion's chemistry; it recognises the single-stranded character of the undamaged strand opposite a helix-distorting adduct, which is why its substrates range from UV photoproducts to bulky chemical adducts. It then recruits TFIIH and hands off to the shared verification and incision machinery.

Because XPC serves only the global-genome branch, losing it gives a distinctive clinical picture: xeroderma pigmentosum group C patients have extreme photosensitivity and hugely raised skin-cancer risk, but usually lack the neurodegeneration seen in groups whose defects also cripple transcription-coupled repair.

Its connection to p53 is transcriptional. XPC mRNA and protein rise after UV damage in a p53-dependent manner, with little induction in p53-deficient cells, and a p53 response element has been mapped to the gene — located, in follow-up work, within the first exon near the translation start rather than in the upstream promoter. [[DDB2]], the other dedicated global-genome sensor, is likewise p53-inducible — the basis for describing p53 as raising global-genome repair capacity as a whole rather than one gene at a time.

## What is uncertain

The p53-dependence of XPC induction was established largely in UV-irradiated fibroblast systems, and how far it carries to the chemical classes in this panel is not something that work addressed. The induction is modest even where it is clean, and in the earlier MG53/p53 study XPC's direction was mixed across the reference compounds — in the induction arm on balance, not because it reliably went up. Whether the mapped exon-1 element is the operative one in all contexts is unresolved.

More fundamentally, XPC mRNA is a poor proxy for repair capacity. XPC acts stoichiometrically as a sensor, its protein is regulated by damage-induced ubiquitination, and DDB2 modulates its recruitment — so a change in transcript need not become a change in lesion clearance. Treat XPC here as a reporter that p53 engaged its repair arm, not as a measure of how much repair happened.

## References

- Sugasawa et al., 1998, *Molecular Cell* — identified the XPC complex as the initiator of global-genome nucleotide-excision repair.
- Araki et al., 2001, *Journal of Biological Chemistry* — identified centrin-2 as the third subunit of the XPC–RAD23B complex.
- Adimoolam & Ford, 2002, *PNAS* — showed XPC mRNA and protein are induced after UV in a p53-dependent manner, and reported a putative p53 response element upstream of the transcription start site.
- Hastak et al., 2012, *Genes & Cancer* — mapped p53 binding at the XPC locus to the first exon at the translation start, and did not reproduce binding at the earlier upstream element in cells.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.44× (z +17.7, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.571× (z -8.0, q 9e-13, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC90B]] (+0.74, fdr 7e-06), [[ACTA2]] (+0.71, fdr 7e-06), [[RPS27L]] (+0.70, fdr 7e-06); moves opposite to [[ST6GALNAC4]] (-0.60, fdr 9e-05), [[HDAC1]] (-0.60, fdr 8e-05), [[SKP2]] (-0.60, fdr 3e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TP53]] → it (grade A ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7837.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.44×** | +17.7 | 0e+00 | 47/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.47×** | +12.9 | 2e-35 | 48/48 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +12.1 | 3e-31 | 45/48 (C32, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.91×** | +8.9 | 1e-16 | 45/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +8.1 | 8e-14 | 35/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +8.0 | 2e-13 | 42/50 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.72×** | +7.7 | 8e-13 | 46/48 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.62×** | +6.9 | 4e-10 | 42/48 (SW48, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +6.4 | 8e-09 | 36/48 (NCI-H460, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +5.7 | 7e-07 | 35/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +5.3 | 5e-06 | 31/47 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.49×** | +5.3 | 6e-06 | 31/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +5.1 | 2e-05 | 26/48 (A549, A-172, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.27×** | +4.8 | 8e-05 | 27/48 (A549, SW48, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.38×** | +4.6 | 1e-04 | 23/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.5 | 2e-04 | 24/48 (C32, SW48, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7837.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.571×** | -8.0 | 9e-13 | 34/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.583×** | -7.7 | 5e-12 | 35/47 (SW1417, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.601×** | -7.2 | 8e-11 | 34/48 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.618×** | -6.8 | 1e-09 | 38/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.471×** | -5.6 | 2e-06 | 35/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.505×** | -5.1 | 4e-05 | 34/48 (SW480, SW 1271, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.719×** | -4.7 | 2e-04 | 29/48 (A549, C-33 A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.725×** | -4.6 | 4e-04 | 25/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.732×** | -4.4 | 6e-04 | 23/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.731×** | -4.3 | 0.001 | 22/47 (LoVo, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.624×** | -3.5 | 0.024 | 20/44 (A-427, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.852× | -3.1 | 0.081 | 18/48 (A-427, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7837. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 76.9 | 13 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +12.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.373× (z -8.7) |
| [[LS 180 (line)]] | wt | 116 | 7 (1 ⚠) | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +13.6) | [[Digitoxin (drug)]] 5 µM 0.282× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.356× (z -9.2) |
| [[SW480 (line)]] | alt | 67.9 | 7 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +15.6) | [[Digitoxin (drug)]] 5 µM 0.347× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.349× (z -13.6) |
| [[LoVo (line)]] | wt | 143 | 6 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +20.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.250× (z -13.0) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.370× (z -9.7) |
| [[C32 (line)]] | wt | 59.8 | 9 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.96× (z +15.7) | — |
| [[LOX-IMVI (line)]] | wt | 80.0 | 8 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +11.2) | [[Auranofin (drug)]] 5 µM 0.365× (z -8.8) |
| [[SW48 (line)]] | wt | 116 | 7 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 106 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +11.6) | — |
| [[RKO (line)]] | wt | 127 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.77× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0922× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[A-427 (line)]] | wt | 122 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.39× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.483× (z -8.7) |
| [[A498 (line)]] | wt | 65.1 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 43.1 | 2 | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.17× (z +9.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -15.6) |
| [[A549 (line)]] | wt | 142 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.49× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.360× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 67.0 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 5.12× (z +10.5) | [[Digitoxin (drug)]] 5 µM 0.235× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.266× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 34.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +14.4) | — |
| [[HS-578T (line)]] | alt | 38.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +12.3) | [[Digitoxin (drug)]] 5 µM 0.317× (z -8.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 64.0 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +11.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.326× (z -10.0) |
| [[KATO III (line)]] | alt | 72.8 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.76× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.376× (z -9.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 41.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +18.3) | — |
| [[HepG2_C3A (line)]] | wt | 55.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 46.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +14.6) | [[Lonafarnib (drug)]] 5 µM 0.0740× (z -11.2) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 47.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 80.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 39.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +13.1) | — |
| [[SNU-1 (line)]] | wt | 84.5 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.21× (z +12.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.37× (z +9.2) | — |
| [[AsPC-1 (line)]] | alt | 29.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +10.9) | — |
| [[BT-474 (line)]] | alt | 63.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +11.5) | — |
| [[C-33 A (line)]] | alt | 85.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.329× (z -9.6) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 17.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +9.8) | — |
| [[CHP-212 (line)]] | wt | 73.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 41.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +11.5) | — |
| [[HCT15 (line)]] | alt | 59.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 31.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +12.1) | — |
| [[NCI-H2030 (line)]] | alt | 45.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.331× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 58.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +12.4) | — |
| [[Panc 03.27 (line)]] | alt | 46.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 63.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 38.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.298× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 51.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +11.7) | — |
| [[SNU-423 (line)]] | alt | 48.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.311× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 120 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.133× (z -9.7) |
| [[SW1417 (line)]] | alt | 78.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -14.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7837), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC90B]] | +0.74 | +0.78 / +0.61 | both halves | 7e-06 |  |
| [[ACTA2]] | +0.71 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[RPS27L]] | +0.70 | +0.70 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[SPATA18]] | +0.69 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[MDM2]] | +0.68 | +0.60 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[LACC1]] | +0.68 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[CCDC174]] | +0.67 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[ZC3H6]] | +0.66 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[TRIP11]] | +0.66 | +0.77 / +0.49 | both halves | 1e-05 |  |
| [[DCP1B]] | +0.66 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[PBDC1]] | +0.66 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[CCAR1]] | +0.66 | +0.77 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC4]] | -0.60 | -0.64 / -0.36 | both halves | 9e-05 |  |
| [[HDAC1]] | -0.60 | -0.67 / -0.37 | both halves | 8e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[SKP2]] | -0.60 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[CS]] | -0.59 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[TUBB]] | -0.58 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[TECR]] | -0.57 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[PIK3R2]] | -0.57 | -0.64 / -0.37 | both halves | 8e-05 |  |
| [[COLGALT1]] | -0.56 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[JAM3]] | -0.56 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[AGO1]] | -0.55 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[TMEM97]] | -0.55 | -0.56 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 1, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | A | TP53 activity raises XPC's level | recorded loss-of-function mutation of TP53 in 33 lines vs 17 not recorded | 1.75× lower at baseline in the TP53-altered lines | 0.048 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[TOP2A]] | B | TOP2A activity lowers XPC's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.8% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens XPC's drug response | lines that do not express PINCR (29) vs lines expressing it (21) | the lines without PINCR respond 0.89× as strongly (z diff +0.70); strongest at Harringtonine 0.5 µM: 1.57x vs 2.34x (z diff +2.7) | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; artifact flags |
| [[PINCR]] | B | PINCR activity raises XPC's level | lines that do not express PINCR (29) vs lines expressing it (21) | 1.50× lower at baseline in the lines without PINCR | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[EDA2R]] | B | EDA2R activity raises XPC's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.21× lower at baseline in the lines without EDA2R | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[FAS]] | B | FAS activity raises XPC's level | lines that do not express FAS (8) vs lines expressing it (42) | 1.27× lower at baseline in the lines without FAS | 0.093 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent |
| [[TYMSOS]] | C | TYMSOS activity raises XPC's level | lines that do not express TYMSOS (3) vs lines expressing it (47) | 2.11× lower at baseline in the lines without TYMSOS | 0.041 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD4; also absent: FOXP4-AS1, ENSG00000261341, CCNP; maybe low, not absent |
| [[TP53]] | C | TP53 activity strengthens XPC's drug response | recorded loss-of-function mutation of TP53 in 33 lines vs 17 not recorded | the TP53-altered lines respond 0.79× as strongly (z diff +0.80); strongest at Doxorubicin (hydrochloride) 5 µM: 1.57x vs 2.33x (z diff +2.7) | 0.890 over the table, 0.072 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.729). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.8, 35.8); signed map (41.6, -23.7). **Vector** length 134, 47.4% of its response variance represented; |z| ≥ 3 in 1,406 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.56 to 6); *apoptosis* (hallmark, mean cos +0.56 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +11.2 | +12.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.9 | +17.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +8.9 | +6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.3 | +7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +6.8 | +6.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.1 | +5.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +4.7 | +4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.0 | +3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.7 | +2.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -7.4 | +2.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.9 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.5 | -2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.4 | +4.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.9 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -5.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.5 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | XPC complex subunit, DNA damage recognition and repair factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:14,145,147-14,178,621 (-) |
| Ensembl biotype | protein_coding |
| Also known as | XPCC, RAD4 |
| Gene groups (HGNC) | Xeroderma pigmentosum complementation groups |
| Hallmark sets | DNA_REPAIR, P53_PATHWAY |
| Reactome | 8 pathways, smallest: DNA Damage Recognition in GG-NER; Formation of Incision Complex in GG-NER; SUMOylation of DNA damage response and repair proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01831](https://www.uniprot.org/uniprotkb/Q01831) (DNA repair protein complementing XP-C cells):

> Involved in global genome nucleotide excision repair (GG-NER) by acting as damage sensing and DNA-binding factor component of the XPC complex. Has only a low DNA repair activity by itself which is stimulated by RAD23B and RAD23A. Has a preference to bind DNA containing a short single-stranded segment but not to damaged oligonucleotides. This feature is proposed to be related to a dynamic sensor function: XPC can rapidly screen duplex DNA for non-hydrogen-bonded bases by forming a transient …

**Summary**, from NCBI Gene [7508](https://www.ncbi.nlm.nih.gov/gene/7508):

> The protein encoded by this gene is a key component of the XPC complex, which plays an important role in the early steps of global genome nucleotide excision repair (NER). The encoded protein is important for damage sensing and DNA binding, and shows a preference for single-stranded DNA. Mutations in this gene or some other NER components can result in Xeroderma pigmentosum, a rare autosomal recessive disorder characterized by increased sensitivity to sunlight with the development of carcinomas …

**Accessions** — [HGNC:12816](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12816) · Entrez [7508](https://www.ncbi.nlm.nih.gov/gene/7508) · UniProt [Q01831](https://www.uniprot.org/uniprotkb/Q01831) · Ensembl [ENSG00000154767](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154767)

## Data

Gene col 7837: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7837); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7837, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7837]; `tensor/DDL_lfc|DDL_z.npy` [7837]; `embed/gene_vectors.npy` [7837]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7837 or target_col == 7837). Every well: [[XPC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/XPC.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
