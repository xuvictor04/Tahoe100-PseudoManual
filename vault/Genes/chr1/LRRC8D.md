---
symbol: "LRRC8D"
type: "gene"
col: 10121
ensembl_id: "ENSG00000171492"
name: "leucine rich repeat containing 8 VRAC subunit D"
location: "1p22.2"
module: 18
arm: "+"
pooled_cpm: 61.62
n_lines_expressing: 47
n_dd_up: 7
n_dd_down: 21
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 11
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# LRRC8D

*leucine rich repeat containing 8 VRAC subunit D* — 1p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.44× (z +7.9, q 1e-12, up in 29 of 45 measured lines) ⚠ cell-cycle shift, explains ~69% of this change. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.35× (z +4.1, q 0.007, up in 20 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (15 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.322× (z -17.1, q 0e+00, down in 38 of 45 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.677× (z -8.3, q 7e-15, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRTG]] (+0.65, fdr 7e-06), [[TARBP1]] (+0.64, fdr 1e-05), [[RIOX2]] (+0.61, fdr 1e-05); moves opposite to [[TOX4]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CRACD]] → it (grade B ⚠); 11 go from it, the strongest it → [[MACROD1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10121.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.44×** | +7.9 | 1e-12 | 29/45 (HT-29, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.48×** | +6.0 | 6e-07 | 29/45 (HT-29, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.39×** | +5.0 | 1e-04 | 28/45 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 0.007 | 20/44 (HS-578T, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.7 | 0.021 | 20/45 (HS-578T, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.023 | 21/45 (SW 900, SHP-77, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +3.5 | 0.035 | 19/45 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.048 | 22/44 (A-427, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10121.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.322×** | -17.1 | 0e+00 | 38/45 (PANC-1, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.385×** | -14.4 | 8e-45 | 39/44 (PANC-1, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.593×** | -11.1 | 2e-26 | 29/45 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.473×** | -10.2 | 4e-22 | 32/43 (C-33 A, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.523×** | -8.9 | 5e-17 | 24/39 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.561×** | -8.7 | 3e-16 | 29/45 (NCI-H460, SNU-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.677×** | -8.3 | 7e-15 | 30/45 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.612×** | -7.4 | 1e-11 | 29/44 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.592×** | -7.3 | 2e-11 | 28/41 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.653×** | -6.4 | 8e-09 | 27/45 (A-427, HT-29, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.460×** | -6.1 | 5e-08 | 28/46 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **0.647×** | -6.0 | 1e-07 | 26/44 (LoVo, NCI-H2030, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.682×** | -5.8 | 4e-07 | 28/45 (HT-29, SW48, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.697×** | -5.4 | 2e-06 | 26/45 (SW1417, SW480, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.714×** | -5.1 | 1e-05 | 28/44 (PANC-1, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.805×** | -3.0 | 0.083 | 17/45 (HS-578T, SW480, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.688×** | -2.9 | 0.089 | 14/44 (SW48, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10121. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 114 | 0 | 13 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -36.8) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 73.4 | 0 | 11 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0775× (z -32.9) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 107 | 1 (1 ⚠) | 9 (8 ⚠) | [[TAK-901 (drug)]] 5 µM 8.01× (z +10.7) ⚠ cell-cycle shift, explains ~28% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -15.4) |
| [[HT-29 (line)]] | alt | 68.4 | 3 (3 ⚠) | 6 (4 ⚠) | [[Selinexor (drug)]] 5 µM 3.15× (z +15.2) ⚠ cell-cycle shift, explains ~69% of this change | [[Digitoxin (drug)]] 5 µM 0.122× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.280× (z -12.0) |
| [[SW1417 (line)]] | alt | 96.9 | 1 (1 ⚠) | 8 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.2) ⚠ cell-cycle shift, explains ~72% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -20.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW480 (line)]] | alt | 81.5 | 0 | 9 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.192× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 67.9 | 0 | 7 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.260× (z -12.9) |
| [[KATO III (line)]] | alt | 75.5 | 2 (2 ⚠) | 5 (5 ⚠) | [[Selinexor (drug)]] 5 µM 2.28× (z +10.8) ⚠ cell-cycle shift, explains ~69% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.157× (z -17.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A498 (line)]] | wt | 94.0 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -27.6) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -9.8) |
| [[LoVo (line)]] | wt | 61.3 | 0 | 6 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -19.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H1573 (line)]] | alt | 48.9 | 1 (1 ⚠) | 5 (4 ⚠) | [[Selinexor (drug)]] 5 µM 2.24× (z +9.1) ⚠ cell-cycle shift, explains ~69% of this change | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -20.1) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 58.5 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -23.3) ⚠ cell-cycle shift, explains ~72% of this change |
| [[RKO (line)]] | wt | 80.6 | 0 | 6 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0846× (z -18.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 94.1 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.151× (z -14.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.306× (z -8.8) |
| [[C-33 A (line)]] | alt | 160 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0929× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.307× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 44.8 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -18.4) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 49.8 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.4) ⚠ cell-cycle shift, explains ~72% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -11.2) |
| [[SNU-1 (line)]] | wt | 72.9 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0705× (z -23.4) ⚠ cell-cycle shift, explains ~72% of this change |
| [[AN3 CA (line)]] | alt | 99.5 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0696× (z -14.4) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 60.3 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -12.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SHP-77 (line)]] | alt | 84.7 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.208× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A549 (line)]] | wt | 71.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -16.7) ⚠ cell-cycle shift, explains ~72% of this change |
| [[HepG2_C3A (line)]] | wt | 58.7 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.222× (z -10.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[Hs 766T (line)]] | wt | 64.6 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.264× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -9.2) |
| [[LS 180 (line)]] | wt | 64.8 | 1 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.72× (z +11.8) ⚠ cell-cycle shift, explains ~69% of this change | [[Digitoxin (drug)]] 5 µM 0.233× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HEC-1-A (line)]] | alt | 67.1 | 2 (2 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.23× (z +11.9) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[J82 (line)]] | alt | 113 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.376× (z -9.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H1792 (line)]] | alt | 98.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -11.6) ⚠ cell-cycle shift, explains ~72% of this change |
| [[NCI-H661 (line)]] | alt | 62.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0331× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[C32 (line)]] | wt | 49.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.253× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[COLO 205 (line)]] | alt | 34.5 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.91× (z +11.7) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[H4 (line)]] | wt | 24.9 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.144× (z -8.9) |
| [[HCT15 (line)]] | alt | 38.2 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.75× (z +10.4) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[HS-578T (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -10.0) ⚠ cell-cycle shift, explains ~72% of this change |
| [[LOX-IMVI (line)]] | wt | 31.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -11.1) ⚠ cell-cycle shift, explains ~72% of this change |
| [[SK-MEL-2 (line)]] | alt | 48.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -19.5) ⚠ cell-cycle shift, explains ~72% of this change |
| [[A-172 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10121), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRTG]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[TARBP1]] | +0.64 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[RIOX2]] | +0.61 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[KIAA1549]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[TSEN2]] | +0.59 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[SFXN4]] | +0.59 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[CAMKMT]] | +0.59 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[HDDC2]] | +0.59 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[CDIN1]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[PTPN4]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[FXN]] | +0.58 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[STX18-AS1]] | +0.58 | +0.55 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOX4]] | -0.49 | -0.50 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRACD]] | B | CRACD activity raises LRRC8D's level | lines that do not express CRACD (12) vs lines expressing it (38) | 2.44× lower at baseline in the lines without CRACD | 0.004 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |
| [[PDE3B]] | B | PDE3B activity raises LRRC8D's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 1.81× lower at baseline in the lines without PDE3B | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[MCOLN2]] | B | MCOLN2 activity raises LRRC8D's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.36× lower at baseline in the lines without MCOLN2 | 0.083 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MACROD1]] | C | LRRC8D activity raises MACROD1's level | lines that do not express LRRC8D (3) vs lines expressing it (47) | 2.65× lower at baseline in the lines without LRRC8D | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PPFIBP2, USP31, EID2; maybe low, not absent; its own permutation p |
| [[VWA8]] | C | LRRC8D activity raises VWA8's level | lines that do not express LRRC8D (3) vs lines expressing it (47) | 2.54× lower at baseline in the lines without LRRC8D | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PPFIBP2, USP31, EID2; maybe low, not absent; its own permutation p |
| [[TGFBRAP1]] | C | LRRC8D activity raises TGFBRAP1's level | lines that do not express LRRC8D (3) vs lines expressing it (47) | 2.06× lower at baseline in the lines without LRRC8D | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PPFIBP2, USP31, EID2; maybe low, not absent; its own permutation p |
| [[VPS54]] | C | LRRC8D activity raises VPS54's level | lines that do not express LRRC8D (3) vs lines expressing it (47) | 1.48× lower at baseline in the lines without LRRC8D | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PPFIBP2, USP31, EID2; maybe low, not absent; its own permutation p |
| [[TMTC4]] | C | LRRC8D activity raises TMTC4's level | lines that do not express LRRC8D (3) vs lines expressing it (47) | 2.73× lower at baseline in the lines without LRRC8D | 0.061 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PPFIBP2, USP31, EID2; maybe low, not absent |
| [[KIAA1549]] | C | LRRC8D activity raises KIAA1549's level | lines that do not express LRRC8D (3) vs lines expressing it (47) | 2.52× lower at baseline in the lines without LRRC8D | 0.067 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PPFIBP2, USP31, EID2; maybe low, not absent |
| [[CAMKMT]] | C | LRRC8D activity raises CAMKMT's level | lines that do not express LRRC8D (3) vs lines expressing it (47) | 2.83× lower at baseline in the lines without LRRC8D | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PPFIBP2, USP31, EID2; maybe low, not absent; its own permutation p |
| [[LTV1]] | C | LRRC8D activity raises LTV1's level | lines that do not express LRRC8D (3) vs lines expressing it (47) | 2.33× lower at baseline in the lines without LRRC8D | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PPFIBP2, USP31, EID2; maybe low, not absent; its own permutation p |
| [[GCFC2]] | C | LRRC8D activity raises GCFC2's level | lines that do not express LRRC8D (3) vs lines expressing it (47) | 2.23× lower at baseline in the lines without LRRC8D | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PPFIBP2, USP31, EID2; maybe low, not absent; its own permutation p |
| [[DCAF17]] | C | LRRC8D activity raises DCAF17's level | lines that do not express LRRC8D (3) vs lines expressing it (47) | 1.83× lower at baseline in the lines without LRRC8D | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PPFIBP2, USP31, EID2; maybe low, not absent; its own permutation p |
| [[CLASP2]] | C | LRRC8D activity raises CLASP2's level | lines that do not express LRRC8D (3) vs lines expressing it (47) | 1.75× lower at baseline in the lines without LRRC8D | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PPFIBP2, USP31, EID2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.1, -40.1); signed map (-7.4, -53.6). **Vector** length 101, 28.4% of its response variance represented; |z| ≥ 3 in 1,110 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +7.3 | +7.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.0 | +3.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +5.6 | +6.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.3 | +2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +0.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +0.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -3.7 | -10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -3.7 | -8.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.3 | -5.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.3 | -2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.5 | -0.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.5 | -2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -6.4 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 8 VRAC subunit D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.2 — chr1:89,821,014-89,936,611 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10470; previously LRRC5 |
| Gene groups (HGNC) | Volume regulated anion channel subunits |
| Reactome | 2 pathways, smallest: Miscellaneous transport and binding events; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L1W4](https://www.uniprot.org/uniprotkb/Q7L1W4) (Volume-regulated anion channel subunit LRRC8D):

> Non-essential component of the volume-regulated anion channel (VRAC, also named VSOAC channel), an anion channel required to maintain a constant cell volume in response to extracellular or intracellular osmotic changes. The VRAC channel conducts iodide better than chloride and can also conduct organic osmolytes like taurine. Plays a redundant role in the efflux of amino acids, such as aspartate, in response to osmotic stress. LRRC8A and LRRC8D are required for the uptake of the drug cisplatin. …

**Summary**, from NCBI Gene [55144](https://www.ncbi.nlm.nih.gov/gene/55144):

> Enables volume-sensitive anion channel activity. Involved in several processes, including aspartate transmembrane transport; protein hexamerization; and taurine transmembrane transport. Located in cytoplasm and plasma membrane. Part of monoatomic ion channel complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16992](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16992) · Entrez [55144](https://www.ncbi.nlm.nih.gov/gene/55144) · UniProt [Q7L1W4](https://www.uniprot.org/uniprotkb/Q7L1W4) · Ensembl [ENSG00000171492](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171492)

## Data

Gene col 10121: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10121); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10121, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10121]; `tensor/DDL_lfc|DDL_z.npy` [10121]; `embed/gene_vectors.npy` [10121]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10121 or target_col == 10121). Every well: [[LRRC8D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC8D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
