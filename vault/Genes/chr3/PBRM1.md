---
symbol: "PBRM1"
type: "gene"
col: 8817
ensembl_id: "ENSG00000163939"
name: "polybromo 1"
location: "3p21.1"
module: 51
arm: "+"
pooled_cpm: 121.12
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051", "written"]
generated_by: "tahoemap"
---

# PBRM1

*polybromo 1* — 3p21.1

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> PBRM1 encodes BAF180, the subunit that defines the PBAF chromatin-remodelling complex and aims it at acetylated histones.

## What it is

BAF180 is a reader module built at scale: six bromodomains, two BAH domains and an HMG box, which together direct the PBAF form of the SWI/SNF remodelling complex to particular acetylated nucleosomes. It is a tumour suppressor, and in clear-cell renal cell carcinoma the most frequently mutated gene after VHL, usually by truncation; inactivating mutations also occur in breast cancer. Its link to p53 runs through transcription rather than through p53 itself: BAF180 binds the CDKN1A promoter and is required for p21 induction and G1 arrest after TGF-beta and ionising radiation, and BAF180 with BRD7 is needed for p53-dependent transcription of the targets that drive senescence.

## What is uncertain

The regulon here holds only a handful of targets and overlaps p53's own, so the score sits close to a re-reading of [[CDKN1A]] and collinear with [[TP53]]'s. The direction of PBRM1's effect on p21 is not settled either: required for induction where it was first shown, reported as restraining elsewhere, so context decides. mRNA is a weak proxy for a complex subunit whose function depends on assembly and on chromatin acetylation state.

## References

- Xia et al., 2008, Cancer Research — BAF180 binds the p21 promoter and is required for p21 induction and G1 arrest; truncating mutations found in breast cancer.
- Burrows et al., 2010, PNAS — BRD7 and BAF180 are required for p53-dependent transcription of targets driving replicative senescence.
- Varela et al., 2011, Nature — exome sequencing identified PBRM1 as the second major mutated gene in clear-cell renal cell carcinoma.
- Miao et al., 2018, Science — PBRM1 loss-of-function was associated with clinical benefit from immune checkpoint therapy in renal cell carcinoma; later cohorts have not reproduced this consistently.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.62× (z +15.1, q 0e+00, up in 40 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.34× (z +8.7, q 5e-16, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.644× (z -19.3, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP16]] (+0.64, fdr 1e-05), [[SMARCB1]] (+0.64, fdr 9e-06), [[STAG1]] (+0.64, fdr 7e-06); moves opposite to [[NDUFAF7]] (-0.63, fdr 2e-05), [[DHRS1]] (-0.63, fdr 1e-05), [[ZFYVE27]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8817.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +15.1 | 0e+00 | 40/49 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +11.9 | 5e-30 | 28/44 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +8.7 | 5e-16 | 31/48 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.27×** | +6.9 | 7e-10 | 27/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | 1.18× | +4.9 | 1e-04 | 17/48 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.17× | +4.9 | 1e-04 | 22/49 (LoVo, SW1417, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 1.10× | +4.3 | 0.002 | 16/48 (NCI-H2347, RKO, …) | rises with dose | composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.002 | 16/49 (LoVo, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.14× | +4.0 | 0.003 | 4/49 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.10× | +4.0 | 0.003 | 1/48 (AN3 CA) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.15× | +4.0 | 0.003 | 9/50 (HOP62, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.05 µM |  | 1.13× | +3.8 | 0.008 | 5/48 (Panc 03.27, HOP62, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.23×** | +3.3 | 0.040 | 19/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.3 | 0.040 | 6/48 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.03× | +3.3 | 0.043 | 0/50 | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.045 | 7/48 (LOX-IMVI, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.053 | 16/50 (SK-MEL-2, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Omeprazole (drug)]] 5 µM |  | 1.10× | +3.1 | 0.068 | 3/48 (J82, HOP62, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 1.10× | +3.0 | 0.080 | 3/49 (HOP62, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8817.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.644×** | -19.3 | 0e+00 | 44/49 (NCI-H2030, SHP-77, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.564×** | -17.8 | 0e+00 | 48/48 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.747×** | -12.8 | 2e-35 | 37/48 (J82, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.692×** | -11.5 | 3e-28 | 45/48 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.708×** | -10.7 | 8e-25 | 42/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.791×** | -7.3 | 2e-11 | 33/49 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.792×** | -7.2 | 4e-11 | 26/48 (NCI-H2030, LoVo, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.795×** | -7.2 | 6e-11 | 28/48 (NCI-H2030, PANC-1, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.806×** | -6.5 | 7e-09 | 24/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.817×** | -6.3 | 2e-08 | 25/48 (HEC-1-A, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.877× | -5.8 | 4e-07 | 13/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.703×** | -5.7 | 5e-07 | 27/49 (J82, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.838× | -5.5 | 2e-06 | 21/48 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.835× | -5.4 | 3e-06 | 23/50 (HEC-1-A, C-33 A, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.843× | -5.3 | 4e-06 | 16/48 (Panc 03.27, J82, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.858× | -4.8 | 7e-05 | 17/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.899× | -4.7 | 1e-04 | 16/48 (A-427, HOP62, …) | top dose only |  |
| [[Infigratinib (drug)]] 5 µM |  | **0.794×** | -3.7 | 0.005 | 13/48 (H4, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.930× | -3.2 | 0.032 | 5/48 (NCI-H460, NCI-H2347, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.912× | -2.9 | 0.099 | 4/48 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8817. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 189 | 1 (1 ⚠) | 8 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.61× (z +9.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -15.0) |
| [[PANC-1 (line)]] | alt | 112 | 3 (2 ⚠) | 6 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 1.73× (z +9.6) | [[Belinostat (drug)]] 0.5 µM 0.506× (z -12.5) |
| [[SW480 (line)]] | alt | 142 | 3 (3 ⚠) | 6 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +15.5) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -13.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.644× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 144 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +15.3) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.85× (z +9.1) | [[Selinexor (drug)]] 5 µM 0.622× (z -10.2) |
| [[HOP62 (line)]] | alt | 129 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 1.86× (z +8.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -9.8) |
| [[J82 (line)]] | alt | 151 | 0 | 4 | — | [[Belinostat (drug)]] 0.5 µM 0.411× (z -14.8) |
| [[NCI-H1573 (line)]] | alt | 80.6 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.433× (z -12.3) |
| [[A-172 (line)]] | wt | 115 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 1.97× (z +9.1) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 0.5 µM 0.465× (z -10.7) |
| [[A498 (line)]] | wt | 54.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +10.5) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.599× (z -9.6) |
| [[A549 (line)]] | wt | 84.1 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.4) ⚠ cell-cycle shift, explains ~69% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -10.3) |
| [[AN3 CA (line)]] | alt | 171 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.244× (z -11.8) |
| [[C-33 A (line)]] | alt | 227 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.462× (z -10.9) |
| [[HS-578T (line)]] | alt | 129 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.575× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 160 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.637× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 156 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -17.5) |
| [[NCI-H460 (line)]] | wt | 115 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -14.4) |
| [[Panc 03.27 (line)]] | alt | 117 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.95× (z +9.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -12.8) |
| [[RKO (line)]] | wt | 115 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +12.5) ⚠ cell-cycle shift, explains ~69% of this change | [[Belinostat (drug)]] 0.5 µM 0.484× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 159 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.97× (z +9.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 138 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.0) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.93× (z +8.6) | [[Belinostat (drug)]] 0.5 µM 0.449× (z -10.9) |
| [[SNU-423 (line)]] | alt | 145 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -13.0) |
| [[A-427 (line)]] | wt | 148 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.467× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.621× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 73.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.07× (z +8.6) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 0.5 µM 0.408× (z -11.1) |
| [[H4 (line)]] | wt | 79.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -10.1) |
| [[HT-29 (line)]] | alt | 99.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.06× (z +10.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.650× (z -9.0) |
| [[KATO III (line)]] | alt | 124 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.83× (z +9.8) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.653× (z -9.7) |
| [[LoVo (line)]] | wt | 149 | 1 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 2.48× (z +9.0) ⚠ cell-cycle shift, explains ~5% of this change | [[Belinostat (drug)]] 0.5 µM 0.511× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 100 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.601× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 114 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 155 | 1 | 1 | [[Harringtonine (drug)]] 5 µM 1.80× (z +9.6) | [[Belinostat (drug)]] 0.5 µM 0.503× (z -11.9) |
| [[SNU-1 (line)]] | wt | 146 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.402× (z -10.4) |
| [[BT-474 (line)]] | alt | 115 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.441× (z -10.5) |
| [[CHP-212 (line)]] | wt | 134 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -10.0) |
| [[LS 180 (line)]] | wt | 140 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.514× (z -9.6) |
| [[SHP-77 (line)]] | alt | 119 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -15.8) |
| [[SW 1271 (line)]] | alt | 117 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0725× (z -12.9) |
| [[SW 900 (line)]] | alt | 94.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -9.9) |
| [[SW1417 (line)]] | alt | 72.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.04× (z +9.4) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 89.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 92.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 90.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 103 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 135 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8817), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP16]] | +0.64 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[SMARCB1]] | +0.64 | +0.57 / +0.60 | both halves | 9e-06 | same gene group; pathway: ATP-dependent chromatin remodelers; STRING 999 |
| [[STAG1]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[ZNF644]] | +0.62 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[ZMYM4]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[DPP8]] | +0.61 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[LZIC]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ATRX]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 | STRING 772 |
| [[INO80]] | +0.60 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[SDCBP2-AS1]] | +0.59 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[ZMYND11]] | +0.59 | +0.50 / +0.66 | both halves | 1e-05 | same gene group |
| [[THRAP3]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFAF7]] | -0.63 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[DHRS1]] | -0.63 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[ZFYVE27]] | -0.60 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[FAM89A]] | -0.59 | -0.37 / -0.64 | both halves | 8e-05 |  |
| [[RAB11FIP5]] | -0.58 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[BAHD1]] | -0.57 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[ZNF836]] | -0.56 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[CNOT8]] | -0.55 | -0.36 / -0.58 | both halves | 9e-05 |  |
| [[RNF149]] | -0.55 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[SLIRP]] | -0.55 | -0.11 / -0.64 | ⚠ one half (not replicated) | 0.002 |  |
| [[PMS2P3-1]] | -0.55 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[SEC14L2]] | -0.55 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[UBTD1]] | -0.54 | -0.50 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.636). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-23.6, 12.9); signed map (12.7, -32.4). **Vector** length 126, 36.3% of its response variance represented; |z| ≥ 3 in 1,131 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.7 | +15.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.5 | +11.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.9 | +8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +8.2 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +7.4 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.2 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.4 | +4.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.3 | +2.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.2 | +2.1 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -9.3 | -17.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.1 | -12.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -19.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.3 | -11.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.4 | -7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -6.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -3.5 | -5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -5.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.2 | -1.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | polybromo 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:52,545,352-52,685,917 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BAF180, PB1, SMARCH1 |
| Gene groups (HGNC) | Bromodomain containing; PBAF complex subunits |
| Reactome | 8 pathways, smallest: Formation of the polybromo-BAF (pBAF) complex; SWI/SNF chromatin remodelers; RMTs methylate histone arginines |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86U86](https://www.uniprot.org/uniprotkb/Q86U86) (Protein polybromo-1):

> Involved in transcriptional activation and repression of select genes by chromatin remodeling (alteration of DNA-nucleosome topology). Required for the stability of the SWI/SNF chromatin remodeling complex SWI/SNF-B (PBAF). Acts as a negative regulator of cell proliferation.

**Summary**, from NCBI Gene [55193](https://www.ncbi.nlm.nih.gov/gene/55193):

> This locus encodes a subunit of ATP-dependent chromatin-remodeling complexes. The encoded protein has been identified as in integral component of complexes necessary for ligand-dependent transcriptional activation by nuclear hormone receptors. Mutations at this locus have been associated with primary clear cell renal cell carcinoma. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:30064](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30064) · Entrez [55193](https://www.ncbi.nlm.nih.gov/gene/55193) · UniProt [Q86U86](https://www.uniprot.org/uniprotkb/Q86U86) · Ensembl [ENSG00000163939](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163939)

## Data

Gene col 8817: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8817); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8817, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8817]; `tensor/DDL_lfc|DDL_z.npy` [8817]; `embed/gene_vectors.npy` [8817]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8817 or target_col == 8817). Every well: [[PBRM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/PBRM1.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
