---
symbol: "RAD54B"
type: "gene"
col: 12372
ensembl_id: "ENSG00000197275"
name: "RAD54 homolog B"
location: "8q22.1"
module: 71
arm: "+"
pooled_cpm: 63.82
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 31
n_dd_up_clean: 6
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/071", "written"]
generated_by: "tahoemap"
---

# RAD54B

*RAD54 homolog B* — 8q22.1

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> RAD54B is a SWI2/SNF2-family DNA translocase that works in homologous recombination and has separately been reported as a scaffold promoting MDM2–MDMX-dependent p53 degradation.

## What it is

The paralogue of RAD54L: an ATP-driven double-stranded DNA translocase that binds RAD51 and remodels nucleosomes and branched recombination intermediates. The paralogues are not simply redundant — mouse Rad54b loss alone has little effect on recombination efficiency, and genetic analysis gives them non-overlapping roles despite similar biochemistry. Mutations were found in primary colon cancers and lymphomas, and RAD54B-deficient cells are synthetic-lethal with loss of FEN1. The p53 link is a separate line of work: RAD54B was reported to act as an adapter promoting MDM2–MDMX heterodimer formation and ubiquitin-dependent p53 turnover, rising early after damage and falling once a checkpoint is established.

## What is uncertain

Those two explanations are not separable from this data. Most recombination and cell-cycle genes fall when cells arrest, so the repression is fully expected from [[CDKN1A]]-driven E2F and DREAM shutdown alone, with no feedback interpretation required. The MDM2–MDMX scaffold claim rests on essentially one primary study and has not been broadly replicated; treat it as a lead, not a premise. In the earlier MG53/p53 study its direction was also flagged as internally mixed across compounds, so its sign is less clean than a single summary suggests.

## References

- Hiramoto et al., 1999, Oncogene — found mutations in RAD54B in primary cancers.
- Wesoly et al., 2006, Molecular and Cellular Biology — showed the differential, non-overlapping contributions of the mammalian Rad54 paralogues to recombination, repair and meiosis.
- McManus et al., 2009, PNAS — FEN1 silencing is synthetic-lethal in RAD54B-deficient colorectal cancer cells.
- Yasuhara et al., 2014, Nature Communications — reported Rad54B as a scaffold for MDM2–MDMX-mediated p53 degradation.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.14× (z +14.8, q 0e+00, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.46× (z +7.4, q 3e-11, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.444× (z -15.8, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLQ]] (+0.78, fdr 7e-06), [[SLF1]] (+0.78, fdr 7e-06), [[BLM]] (+0.77, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12372.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **2.14×** | +14.8 | 0e+00 | 43/48 (NCI-H2347, RKO, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.91×** | +12.5 | 1e-33 | 42/48 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.81×** | +11.5 | 3e-28 | 40/48 (NCI-H2347, RKO, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +7.4 | 3e-11 | 31/48 (PANC-1, H4, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.36×** | +6.0 | 2e-07 | 25/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.34×** | +5.4 | 6e-06 | 26/49 (HS-578T, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +5.1 | 3e-05 | 23/48 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.30×** | +4.9 | 9e-05 | 25/48 (HS-578T, SW1417, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.23×** | +4.0 | 0.004 | 17/48 (RKO, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.22×** | +3.9 | 0.005 | 17/48 (RKO, LoVo, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.010 | 17/48 (RKO, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.20× | +3.5 | 0.025 | 21/48 (RKO, J82, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.053 | 16/47 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.053 | 4/48 (LoVo, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.12× | +3.1 | 0.064 | 13/48 (HS-578T, NCI-H23, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.36×** | +3.1 | 0.066 | 5/48 (KATO III, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.066 | 18/47 (CFPAC-1, A549, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.12× | +3.0 | 0.083 | 6/48 (SHP-77, SW1417, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.088 | 12/47 (COLO 205, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.18× | +2.9 | 0.093 | 7/48 (CFPAC-1, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12372.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.444×** | -15.8 | 0e+00 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.515×** | -12.9 | 2e-35 | 39/48 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.491×** | -12.8 | 4e-35 | 32/44 (SHP-77, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.525×** | -12.5 | 9e-34 | 39/48 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.558×** | -11.3 | 1e-27 | 40/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.691×** | -10.2 | 3e-22 | 30/48 (KATO III, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.592×** | -9.8 | 1e-20 | 27/40 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.606×** | -9.7 | 2e-20 | 34/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.608×** | -9.7 | 3e-20 | 36/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.618×** | -9.3 | 5e-19 | 31/49 (NCI-H2030, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.673×** | -7.4 | 7e-12 | 27/47 (COLO 205, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.764×** | -7.4 | 7e-12 | 30/49 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.709×** | -6.7 | 1e-09 | 30/48 (COLO 205, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.710×** | -6.6 | 1e-09 | 30/48 (A-427, LS 180, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.765×** | -5.2 | 7e-06 | 23/48 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.735×** | -5.2 | 8e-06 | 22/48 (LS 180, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[4EGI-1 (drug)]] 5 µM |  | **0.618×** | -4.9 | 4e-05 | 26/48 (HCT15, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 0.852× | -4.4 | 3e-04 | 17/49 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.803×** | -4.2 | 6e-04 | 20/48 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.810×** | -4.1 | 0.001 | 16/48 (HOP62, HT-29, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.875× | -3.7 | 0.006 | 10/48 (CFPAC-1, NCI-H23, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.64 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12372. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 93.3 | 0 | 11 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.252× (z -13.4) |
| [[COLO 205 (line)]] | alt | 113 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0572× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -15.4) |
| [[PANC-1 (line)]] | alt | 85.0 | 0 | 9 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.241× (z -19.2) |
| [[CFPAC-1 (line)]] | alt | 69.0 | 1 | 7 (2 ⚠) | [[Cobimetinib (drug)]] 5 µM 3.30× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -14.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -13.6) |
| [[NCI-H460 (line)]] | wt | 54.8 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.231× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.266× (z -13.4) |
| [[LS 180 (line)]] | wt | 92.4 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -13.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.265× (z -12.2) |
| [[SHP-77 (line)]] | alt | 70.9 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0487× (z -25.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.295× (z -11.2) |
| [[SW480 (line)]] | alt | 76.9 | 1 (1 ⚠) | 6 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.16× (z +9.5) ⚠ cell-cycle shift, explains ~50% of this change | [[Digitoxin (drug)]] 5 µM 0.286× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -15.0) |
| [[HepG2_C3A (line)]] | wt | 54.5 | 0 | 6 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0741× (z -16.2) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -13.5) |
| [[NCI-H2030 (line)]] | alt | 111 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.328× (z -12.4) |
| [[SW1417 (line)]] | alt | 73.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -14.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.379× (z -9.5) |
| [[LoVo (line)]] | wt | 51.0 | 2 (2 ⚠) | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.79× (z +11.0) ⚠ cell-cycle shift, explains ~50% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.293× (z -13.3) |
| [[RKO (line)]] | wt | 104 | 3 (3 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.74× (z +11.3) ⚠ cell-cycle shift, explains ~50% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.196× (z -13.5) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.336× (z -9.4) |
| [[Hs 766T (line)]] | wt | 35.1 | 1 (1 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.93× (z +9.5) ⚠ cell-cycle shift, explains ~50% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.206× (z -11.0) |
| [[HT-29 (line)]] | alt | 44.7 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.286× (z -10.2) |
| [[J82 (line)]] | alt | 79.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.305× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.415× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 27.4 | 1 (1 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.17× (z +9.7) ⚠ cell-cycle shift, explains ~50% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 32.6 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.48× (z +14.8) ⚠ cell-cycle shift, explains ~50% of this change | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.402× (z -9.0) |
| [[A-427 (line)]] | wt | 52.6 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.459× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.339× (z -9.5) |
| [[A498 (line)]] | wt | 144 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.241× (z -12.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 26.9 | 1 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.45× (z +9.3) ⚠ cell-cycle shift, explains ~50% of this change | [[Dinaciclib (drug)]] 5 µM 0.212× (z -9.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 31.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.29× (z +11.2) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[LOX-IMVI (line)]] | wt | 33.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +10.9) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[SW 900 (line)]] | alt | 36.8 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.33× (z +10.4) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[H4 (line)]] | wt | 52.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -11.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 50.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.324× (z -8.5) |
| [[A-172 (line)]] | wt | 37.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -13.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 73.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -10.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 61.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.308× (z -9.6) |
| [[C-33 A (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0902× (z -20.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 66.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -9.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 75.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.297× (z -8.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 96.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -12.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 39.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.62× (z +9.5) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H23 (line)]] | alt | 56.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[Panc 03.27 (line)]] | alt | 46.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.81× (z +8.5) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[SW 1271 (line)]] | alt | 60.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0453× (z -11.1) |
| [[SW48 (line)]] | wt | 51.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.263× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 78.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12372), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLQ]] | +0.78 | +0.74 / +0.79 | both halves | 7e-06 | STRING 453 |
| [[SLF1]] | +0.78 | +0.71 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[BLM]] | +0.77 | +0.67 / +0.80 | both halves | 7e-06 | STRING 678 |
| [[BRIP1]] | +0.76 | +0.71 / +0.82 | both halves | 7e-06 | STRING 520 |
| [[BARD1]] | +0.76 | +0.67 / +0.79 | both halves | 7e-06 | STRING 467 |
| [[DTL]] | +0.76 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[EXO1]] | +0.75 | +0.67 / +0.79 | both halves | 7e-06 | STRING 740 |
| [[FSBP]] | +0.75 | +0.73 / +0.74 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[RAD54L]] | +0.75 | +0.67 / +0.77 | both halves | 7e-06 | same gene group; STRING 952 |
| [[CEP152]] | +0.74 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[UBE2T]] | +0.74 | +0.66 / +0.79 | both halves | 7e-06 | STRING 463 |
| [[DSCC1]] | +0.74 | +0.65 / +0.75 | both halves | 7e-06 | STRING 512 |
| [[WDHD1]] | +0.74 | +0.67 / +0.77 | both halves | 7e-06 | STRING 648 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises RAD54B's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.01× lower at baseline in the lines without E2F8 | 0.030 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.690). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.5, -49.6); signed map (-40.9, -40.9). **Vector** length 118, 37.7% of its response variance represented; |z| ≥ 3 in 1,511 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.4 | -2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +3.2 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +2.7 | +6.0 |
|  | [[NG25 (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.3 | +0.9 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +7.4 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.0 | +1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +1.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.7 | -11.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.1 | -12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.7 | -12.8 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | -4.5 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -6.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | -4.1 | -3.7 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -3.8 | -4.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | RAD54 homolog B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:94,371,960-94,475,115 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RDH54 |
| Gene groups (HGNC) | SNF2 related family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y620](https://www.uniprot.org/uniprotkb/Q9Y620) (DNA repair and recombination protein RAD54B):

> Multifunctional ATPase that could play with RAD54, a redundant role in homologous recombination (HR), a major pathway for repairing DNA double-strand breaks (DSBs), single-stranded DNA (ssDNA) gaps, and stalled or collapsed replication forks. Could act as a molecular motor during the homology search and guide RAD51 ssDNA along a donor dsDNA thereby changing the homology search from the diffusion-based mechanism to a motor-guided mechanism. Once DNA strand exchange occured, could dissociate …

**Summary**, from NCBI Gene [25788](https://www.ncbi.nlm.nih.gov/gene/25788):

> The protein encoded by this gene belongs to the DEAD-like helicase superfamily. It shares similarity with Saccharomyces cerevisiae RAD54 and RDH54, both of which are involved in homologous recombination and repair of DNA. This protein binds to double-stranded DNA, and displays ATPase activity in the presence of DNA. This gene is highly expressed in testis and spleen, which suggests active roles in meiotic and mitotic recombination. Homozygous mutations of this gene were observed in primary …

**Accessions** — [HGNC:17228](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17228) · Entrez [25788](https://www.ncbi.nlm.nih.gov/gene/25788) · UniProt [Q9Y620](https://www.uniprot.org/uniprotkb/Q9Y620) · Ensembl [ENSG00000197275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197275)

## Data

Gene col 12372: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12372); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12372, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12372]; `tensor/DDL_lfc|DDL_z.npy` [12372]; `embed/gene_vectors.npy` [12372]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12372 or target_col == 12372). Every well: [[RAD54B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/RAD54B.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
