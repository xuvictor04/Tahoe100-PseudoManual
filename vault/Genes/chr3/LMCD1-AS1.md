---
symbol: "LMCD1-AS1"
type: "gene"
col: 13575
ensembl_id: "ENSG00000227110"
name: "LMCD1 antisense RNA 1"
location: "3p26.1"
module: 62
arm: "+"
pooled_cpm: 52.24
n_lines_expressing: 48
n_dd_up: 10
n_dd_down: 33
n_dd_up_clean: 10
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# LMCD1-AS1

*LMCD1 antisense RNA 1* — 3p26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.83× (z +6.4, q 9e-08, up in 35 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.244× (z -15.0, q 0e+00, down in 44 of 46 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AZIN1]] (+0.54, fdr 1e-04), [[FGGY]] (+0.54, fdr 1e-04), [[CLTC]] (+0.51, fdr 4e-04); moves opposite to [[SESN1]] (-0.57, fdr 8e-05), [[HERPUD2]] (-0.55, fdr 2e-05), [[GPX1]] (-0.53, fdr 7e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13575.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.83×** | +6.4 | 9e-08 | 35/46 (A-172, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +5.5 | 1e-05 | 31/46 (A-172, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +5.3 | 2e-05 | 32/46 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +5.1 | 5e-05 | 30/46 (A-172, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +4.7 | 3e-04 | 27/46 (A-172, SNU-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.58×** | +4.6 | 3e-04 | 27/45 (SW480, A-427, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +4.5 | 5e-04 | 26/46 (A-172, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.003 | 26/46 (A-172, LS 180, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.06×** | +4.0 | 0.004 | 28/46 (A-172, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.004 | 25/45 (SW480, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13575.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.244×** | -15.0 | 0e+00 | 44/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.253×** | -14.6 | 1e-45 | 42/46 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.305×** | -12.6 | 3e-34 | 41/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.313×** | -11.9 | 2e-30 | 43/45 (HT-29, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.348×** | -11.2 | 4e-27 | 40/46 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.570×** | -8.5 | 3e-15 | 37/46 (SW 900, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.470×** | -8.0 | 8e-14 | 37/46 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.515×** | -6.8 | 8e-10 | 34/46 (SW 900, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.301×** | -6.7 | 2e-09 | 35/47 (HEC-1-A, SHP-77, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.529×** | -6.5 | 4e-09 | 31/46 (A498, A549, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.316×** | -6.4 | 8e-09 | 35/46 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.539×** | -6.3 | 1e-08 | 34/46 (SK-MEL-2, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.547×** | -6.2 | 3e-08 | 29/45 (HepG2/C3A, J82, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.591×** | -5.6 | 9e-07 | 29/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.598×** | -5.5 | 2e-06 | 26/46 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.807×** | -3.2 | 0.031 | 20/46 (HEC-1-A, A-427, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.575×** | -3.1 | 0.050 | 20/46 (C32, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.751×** | -3.0 | 0.052 | 21/46 (PANC-1, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.752×** | -3.0 | 0.052 | 17/46 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13575. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 63.9 | 1 (1 ⚠) | 14 (6 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.56× (z +9.0) ⚠ position not correctable | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -14.1) |
| [[A-427 (line)]] | wt | 108 | 0 | 14 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0974× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 116 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -15.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -9.9) |
| [[PANC-1 (line)]] | alt | 68.7 | 0 | 12 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.116× (z -18.6) |
| [[SHP-77 (line)]] | alt | 121 | 0 | 10 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.108× (z -19.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -16.5) |
| [[NCI-H460 (line)]] | wt | 48.7 | 0 | 9 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.162× (z -13.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -11.1) |
| [[SW 900 (line)]] | alt | 89.7 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -14.3) |
| [[A549 (line)]] | wt | 101 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -19.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.246× (z -10.2) |
| [[HT-29 (line)]] | alt | 52.9 | 0 | 7 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0485× (z -21.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.175× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 58.1 | 1 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +15.0) ⚠ cell-cycle shift, would explain all of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -13.9) |
| [[SW480 (line)]] | alt | 46.7 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.123× (z -16.7) |
| [[A-172 (line)]] | wt | 19.6 | 6 | 0 | [[Auranofin (drug)]] 5 µM 8.15× (z +12.3) | — |
| [[COLO 205 (line)]] | alt | 47.5 | 2 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 0.5 µM 0.129× (z -13.0) |
| [[J82 (line)]] | alt | 30.7 | 1 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 5 µM 0.0702× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.169× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 83.5 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0823× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 79.8 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -11.0) |
| [[A498 (line)]] | wt | 61.0 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -19.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.268× (z -8.8) |
| [[BT-474 (line)]] | alt | 68.9 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -11.3) |
| [[KATO III (line)]] | alt | 51.4 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.142× (z -14.3) |
| [[LS 180 (line)]] | wt | 33.0 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.134× (z -13.1) |
| [[C32 (line)]] | wt | 60.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0636× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -9.5) |
| [[HCT15 (line)]] | alt | 32.9 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +9.8) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -9.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 51.2 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.0411× (z -18.1) ⚠ toxic |
| [[LoVo (line)]] | wt | 18.9 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.93× (z +17.2) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 5 µM 0.220× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.273× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 39.9 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.157× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 50.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +12.5) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 5 µM 0.159× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.199× (z -9.0) |
| [[SNU-1 (line)]] | wt | 44.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.48× (z +10.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.219× (z -9.0) ⚠ toxic |
| [[H4 (line)]] | wt | 35.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.114× (z -9.4) ⚠ toxic |
| [[HOP62 (line)]] | alt | 47.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.156× (z -10.7) |
| [[Hs 766T (line)]] | wt | 40.3 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.161× (z -10.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.184× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 28.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 0.05 µM 0.134× (z -10.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SK-MEL-2 (line)]] | alt | 133 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -13.4) |
| [[SW1417 (line)]] | alt | 35.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.201× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.156× (z -10.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 36.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.168× (z -9.3) |
| [[HS-578T (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.170× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.222× (z -8.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW48 (line)]] | wt | 18.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.96 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13575), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AZIN1]] | +0.54 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[FGGY]] | +0.54 | +0.36 / +0.55 | both halves | 1e-04 |  |
| [[CLTC]] | +0.51 | +0.26 / +0.51 | both halves | 4e-04 |  |
| [[RAD23A]] | +0.51 | +0.54 / +0.25 | both halves | 4e-04 |  |
| [[DNAJB1]] | +0.49 | +0.39 / +0.39 | both halves | 6e-05 |  |
| [[MAP1B]] | +0.49 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[EGF]] | +0.48 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[HSP90AA1]] | +0.48 | +0.48 / +0.43 | both halves | 4e-05 |  |
| [[ANAPC1P4]] | +0.48 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[AIG1]] | +0.48 | +0.31 / +0.50 | both halves | 2e-04 |  |
| [[JAKMIP3]] | +0.48 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[LMCD1]] | +0.48 | +0.34 / +0.42 | both halves | 1e-04 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[NSFL1C]] | +0.47 | +0.30 / +0.34 | both halves | 2e-04 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SESN1]] | -0.57 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[HERPUD2]] | -0.55 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[GPX1]] | -0.53 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[BRMS1L]] | -0.52 | -0.16 / -0.32 | ⚠ not reproduced | 0.001 |  |
| [[GPBP1L1]] | -0.51 | -0.49 / -0.43 | both halves | 4e-05 |  |
| [[PCMTD1]] | -0.50 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[WDR20]] | -0.50 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[POC1B-AS1]] | -0.50 | -0.31 / -0.34 | both halves | 2e-04 | same gene group |
| [[DDX59]] | -0.50 | -0.15 / -0.45 | ⚠ not reproduced | 0.001 |  |
| [[SLC12A9]] | -0.50 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[FBXW4]] | -0.50 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[ANKRA2]] | -0.50 | -0.24 / -0.41 | both halves | 5e-04 |  |
| [[PPM1D]] | -0.49 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[KANSL1]] | -0.48 | -0.36 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises LMCD1-AS1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers LMCD1-AS1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers LMCD1-AS1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction -0.456). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.5, 35.1); signed map (-19.9, -26.2). **Vector** length 98.2, 29.4% of its response variance represented; |z| ≥ 3 in 1,481 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.8 | +4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.0 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.9 | -0.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.4 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +4.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.6 | -11.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.3 | -8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -8.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -6.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -2.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.7 | -1.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | LMCD1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p26.1 — chr3:7,951,263-8,611,924 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44477](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44477) · Entrez [100288428](https://www.ncbi.nlm.nih.gov/gene/100288428) · Ensembl [ENSG00000227110](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227110)

## Data

Gene col 13575: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13575); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13575, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13575]; `tensor/DDL_lfc|DDL_z.npy` [13575]; `embed/gene_vectors.npy` [13575]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13575 or target_col == 13575). Every well: [[LMCD1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMCD1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
