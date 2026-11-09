---
symbol: "HJURP"
type: "gene"
col: 4438
ensembl_id: "ENSG00000123485"
name: "Holliday junction recognition protein"
location: "2q37.1"
module: 22
arm: "+"
pooled_cpm: 62.3
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 50
n_dd_up_clean: 3
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/022", "written"]
generated_by: "tahoemap"
---

# HJURP

*Holliday junction recognition protein* — 2q37.1

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> HJURP is the dedicated chaperone that holds newly made CENP-A and deposits it at centromeres, so it is the gene that decides where new centromeric chromatin is built.

## What it is

HJURP was picked up twice over — once as a protein binding a Holliday-junction-like structure, once as a transcript over-expressed in lung tumours, the source of the alias URLC9. Its real job emerged from CENP-A proteomics: HJURP binds the CENP-A/H4 dimer through a conserved N-terminal domain, keeps it soluble, and loads it into centromeric chromatin in a narrow window at mitotic exit and early G1. Without it, new CENP-A is not deposited, the existing pool is diluted by replication, and kinetochores fail — placing HJURP upstream of the CENP-A reader [[CENPN]] in one assembly pathway. Beyond that the literature is largely correlative: high HJURP associates with poor outcome in several tumour series, a weak basis for functional claims.

## What is uncertain

Nothing establishes HJURP as a p53 target in any direct sense, and in the earlier MG53/p53 study its membership of the p53 repression arm was unstable across cross-fitting folds, so hold it more loosely than the arm's core members. There is also a timing problem: HJURP acts in a short window at mitotic exit, so a 24 h transcript measurement in an arresting population reports cell-cycle distribution rather than centromere assembly. The prognosis literature is expression-correlation, not evidence that HJURP drives those phenotypes.

## References

- Foltz et al., 2009, Cell — showed HJURP mediates centromere-specific assembly of CENP-A nucleosomes.
- Dunleavy et al., 2009, Cell — identified HJURP as a cell-cycle-dependent CENP-A deposition and maintenance factor.
- Shuaib et al., 2010, PNAS — mapped the conserved N-terminal domain through which HJURP binds CENP-A.
- Engeland, 2018, Cell Death and Differentiation — review of p53-p21-DREAM-mediated repression of cell-cycle genes.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.67× (z +5.9, q 2e-06, up in 35 of 46 measured lines) ⚠ transcription drop; cell-cycle shift, would explain all of this change. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 1.39× (z +3.6, q 0.020, up in 20 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 50 drug-doses (19 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.434× (z -13.4, q 6e-38, down in 41 of 46 measured lines) ⚠ cell-cycle shift, explains ~62% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.698× (z -5.7, q 8e-07, down in 26 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF2C]] (+0.90, fdr 7e-06), [[GTSE1]] (+0.90, fdr 7e-06), [[SGO2]] (+0.89, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PBK]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4438.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.67×** | +5.9 | 2e-06 | 35/46 (SW1417, NCI-H2030, …) | all doses, flat | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.30×** | +4.3 | 0.004 | 29/46 (NCI-H23, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.43×** | +4.1 | 0.006 | 24/46 (KATO III, HT-29, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.28×** | +4.1 | 0.006 | 24/46 (Panc 03.27, NCI-H2347, …) | top dose only | composition shift; position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.42×** | +4.0 | 0.006 | 22/45 (NCI-H23, PANC-1, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.38×** | +3.7 | 0.018 | 22/45 (PANC-1, NCI-H23, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.38×** | +3.7 | 0.018 | 21/46 (NCI-H23, KATO III, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.020 | 20/45 (NCI-H23, HOP62, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.34×** | +3.4 | 0.046 | 21/46 (KATO III, HT-29, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +3.3 | 0.058 | 19/46 (PANC-1, NCI-H23, …) | all doses, flat |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.091 | 15/46 (MIA PaCa-2, LoVo, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.094 | 18/46 (SHP-77, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 50 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4438.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.434×** | -13.4 | 6e-38 | 41/46 (LS 180, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.406×** | -10.2 | 6e-22 | 40/46 (SNU-1, A-427, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.491×** | -7.7 | 2e-12 | 29/41 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.496×** | -6.9 | 8e-10 | 32/46 (LOX-IMVI, A-172, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.548×** | -6.8 | 1e-09 | 28/46 (HOP62, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.582×** | -6.1 | 9e-08 | 21/45 (LOX-IMVI, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -5.7 | 8e-07 | 26/45 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **0.594×** | -5.7 | 1e-06 | 26/45 (LOX-IMVI, A549, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.607×** | -5.6 | 1e-06 | 36/46 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.708×** | -5.5 | 2e-06 | 27/46 (A549, H4, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.667×** | -5.5 | 2e-06 | 28/46 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.616×** | -5.5 | 2e-06 | 29/46 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.617×** | -5.4 | 3e-06 | 30/46 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.724×** | -5.1 | 1e-05 | 32/46 (RKO, HCT15, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.718×** | -5.0 | 2e-05 | 32/46 (MIA PaCa-2, PANC-1, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.746×** | -4.7 | 1e-04 | 25/46 (LOX-IMVI, A549, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.662×** | -4.6 | 1e-04 | 28/46 (PANC-1, HOP62, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.668×** | -4.4 | 3e-04 | 23/46 (PANC-1, HCT15, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.669×** | -4.4 | 3e-04 | 27/45 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.725×** | -4.4 | 3e-04 | 26/46 (PANC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.691×** | -4.3 | 4e-04 | 28/46 (HOP62, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.684×** | -4.3 | 4e-04 | 24/45 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.700×** | -4.0 | 0.001 | 24/46 (HCT15, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.700×** | -4.0 | 0.001 | 22/46 (HCT15, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.763×** | -4.0 | 0.001 | 29/46 (PANC-1, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +1.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4438. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 106 | 0 | 11 (7 ⚠) | — | [[Amsacrine (drug)]] 5 µM 0.210× (z -14.2) |
| [[H4 (line)]] | wt | 138 | 0 | 11 (9 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.148× (z -14.2) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.174× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 92.4 | 0 | 11 (7 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.107× (z -19.7) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.198× (z -14.2) |
| [[A498 (line)]] | wt | 90.5 | 0 | 10 (8 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.150× (z -19.5) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -13.7) |
| [[A-172 (line)]] | wt | 63.6 | 0 | 8 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.204× (z -15.7) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.302× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 91.6 | 0 | 8 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.239× (z -13.3) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -12.9) |
| [[HOP62 (line)]] | alt | 168 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -10.7) |
| [[SNU-1 (line)]] | wt | 201 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0379× (z -16.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -10.8) |
| [[LS 180 (line)]] | wt | 39.9 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0413× (z -23.3) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.274× (z -9.4) |
| [[PANC-1 (line)]] | alt | 85.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -8.5) |
| [[C32 (line)]] | wt | 29.7 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0968× (z -18.9) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.307× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 102 | 0 | 3 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.532× (z -12.7) ⚠ position not correctable |
| [[SK-MEL-2 (line)]] | alt | 116 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.372× (z -9.9) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -8.7) |
| [[A-427 (line)]] | wt | 57.4 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.124× (z -20.0) ⚠ cell-cycle shift, explains ~62% of this change |
| [[HCT15 (line)]] | alt | 92.4 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.302× (z -9.6) ⚠ cell-cycle shift, explains ~62% of this change |
| [[KATO III (line)]] | alt | 27.9 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.76× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 43.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -10.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 35.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -8.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.330× (z -8.5) |
| [[AN3 CA (line)]] | alt | 52.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -8.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.275× (z -10.6) ⚠ cell-cycle shift, explains ~62% of this change |
| [[HEC-1-A (line)]] | alt | 48.7 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.252× (z -10.1) ⚠ cell-cycle shift, explains ~73% of this change |
| [[HS-578T (line)]] | alt | 51.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HT-29 (line)]] | alt | 33.2 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.95× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[hTERT-HPNE (line)]] | wt | 36.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.245× (z -8.9) ⚠ cell-cycle shift, explains ~62% of this change |
| [[J82 (line)]] | alt | 50.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 29.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.248× (z -13.4) ⚠ cell-cycle shift, explains ~62% of this change |
| [[NCI-H2030 (line)]] | alt | 56.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.384× (z -9.0) ⚠ cell-cycle shift, explains ~62% of this change |
| [[NCI-H23 (line)]] | alt | 85.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.447× (z -8.9) ⚠ cell-cycle shift, explains ~62% of this change |
| [[NCI-H2347 (line)]] | alt | 29.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 33.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +13.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 66.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -8.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 55.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 52.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4438), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF2C]] | +0.90 | +0.89 / +0.90 | both halves | 7e-06 | STRING 938 |
| [[GTSE1]] | +0.90 | +0.87 / +0.91 | both halves | 7e-06 | pathway: G2/M Transition; STRING 889 |
| [[SGO2]] | +0.89 | +0.85 / +0.91 | both halves | 7e-06 | **novel candidate** |
| [[CDCA8]] | +0.89 | +0.86 / +0.90 | both halves | 7e-06 | STRING 923 |
| [[TACC3]] | +0.88 | +0.88 / +0.89 | both halves | 7e-06 | STRING 620 |
| [[KIF14]] | +0.87 | +0.87 / +0.87 | both halves | 7e-06 | STRING 927 |
| [[KIF18B]] | +0.87 | +0.83 / +0.88 | both halves | 7e-06 | STRING 864 |
| [[AURKB]] | +0.86 | +0.86 / +0.84 | both halves | 7e-06 | STRING 927 |
| [[MKI67]] | +0.86 | +0.85 / +0.88 | both halves | 7e-06 | STRING 946 |
| [[DEPDC1B]] | +0.86 | +0.86 / +0.82 | both halves | 7e-06 | STRING 526 |
| [[BUB1]] | +0.85 | +0.85 / +0.84 | both halves | 7e-06 | STRING 928 |
| [[UBE2C]] | +0.85 | +0.84 / +0.84 | both halves | 7e-06 | STRING 924 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PBK]] | C | PBK activity raises HJURP's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.00× lower at baseline in the lines without PBK | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[FAM72D]] | C | FAM72D activity raises HJURP's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.52× lower at baseline in the lines without FAM72D | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises HJURP's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.49× lower at baseline in the lines without CDCA3, SPDL1 | 0.093 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; co-absent genes |
| [[TP53]] | C | TP53 activity strengthens HJURP's drug response | recorded loss-of-function mutation of TP53 in 30 lines vs 16 not recorded | the TP53-altered lines respond 0.62× as strongly (z diff +1.73); strongest at Idarubicin (hydrochloride) 0.5 µM: 0.79x vs 0.31x (z diff +4.4) | 0.847 over the table, 0.065 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.880). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.3, -56.4); signed map (-50.1, -41.9). **Vector** length 162, 60.8% of its response variance represented; |z| ≥ 3 in 1,469 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.70 to 60); *DREAM G2/M down* (control, mean cos +0.78 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.66 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +5.9 | +5.9 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.0 | +4.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~93% of this change | +4.9 | +3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.6 | +4.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.0 | -2.9 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.3 | +2.0 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +3.3 | +2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.7 | +1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.6 | +3.1 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | +2.5 | +2.7 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -9.0 | -10.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -8.8 | -13.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | -7.0 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -6.4 | -5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.6 | -6.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.4 | -5.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | -5.0 | -5.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.9 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.6 | -4.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.3 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | Holliday junction recognition protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:233,833,416-233,854,566 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp762E1312, URLC9, hFLEG1, FAKTS |
| Reactome | 8 pathways, smallest: Cyclin A/B1/B2 associated events during G2/M transition; Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCD3](https://www.uniprot.org/uniprotkb/Q8NCD3) (Holliday junction recognition protein):

> Centromeric protein that plays a central role in the incorporation and maintenance of histone H3-like variant CENPA at centromeres. Acts as a specific chaperone for CENPA and is required for the incorporation of newly synthesized CENPA molecules into nucleosomes at replicated centromeres. Prevents CENPA-H4 tetramerization and prevents premature DNA binding by the CENPA-H4 tetramer. Directly binds Holliday junctions.

**Summary**, from NCBI Gene [55355](https://www.ncbi.nlm.nih.gov/gene/55355):

> Enables histone binding activity and identical protein binding activity. Involved in CENP-A containing chromatin assembly; chromosome segregation; and regulation of protein-containing complex assembly. Located in kinetochore and nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25444](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25444) · Entrez [55355](https://www.ncbi.nlm.nih.gov/gene/55355) · UniProt [Q8NCD3](https://www.uniprot.org/uniprotkb/Q8NCD3) · Ensembl [ENSG00000123485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123485)

## Data

Gene col 4438: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4438); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4438, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4438]; `tensor/DDL_lfc|DDL_z.npy` [4438]; `embed/gene_vectors.npy` [4438]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4438 or target_col == 4438). Every well: [[HJURP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/HJURP.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
