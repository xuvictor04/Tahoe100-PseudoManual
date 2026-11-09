---
symbol: "RAB6B"
type: "gene"
col: 7853
ensembl_id: "ENSG00000154917"
name: "RAB6B, member RAS oncogene family"
location: "3q22.1"
module: 132
arm: "+"
pooled_cpm: 12.4
n_lines_expressing: 36
n_dd_up: 10
n_dd_down: 19
n_dd_up_clean: 9
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 23
direction_downstream: 15
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# RAB6B

*RAB6B, member RAS oncogene family* — 3q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.80× (z +14.4, q 6e-44, up in 27 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.238× (z -35.0, q 0e+00, down in 32 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPT]] (+0.73, fdr 7e-06), [[WASF3]] (+0.73, fdr 7e-06), [[RIMS3]] (+0.72, fdr 7e-06); moves opposite to [[ANKRD17-DT]] (-0.61, fdr 1e-04), [[INO80D]] (-0.57, fdr 4e-05), [[WARS2-AS1]] (-0.56, fdr 5e-05).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[KIF26A]] → it (grade B ⚠); 15 go from it, the strongest it → [[SNX10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7853.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.80×** | +14.4 | 6e-44 | 27/34 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.24×** | +14.0 | 6e-42 | 26/32 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +8.5 | 4e-15 | 16/33 (NCI-H2347, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.44×** | +6.3 | 4e-08 | 16/33 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.91×** | +5.9 | 5e-07 | 12/33 (J82, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.008 | 9/31 (PANC-1, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.008 | 13/33 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | 1.17× | +3.7 | 0.013 | 8/33 (LoVo, HOP62, …) | top dose only | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.027 | 9/33 (SK-MEL-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.032 | 2/32 (SW480, Panc 03.27) | rises with dose | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.22×** | +3.4 | 0.039 | 7/32 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.1 | 0.093 | 10/33 (PANC-1, Panc 03.27, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7853.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.238×** | -35.0 | 0e+00 | 32/32 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.268×** | -21.9 | 0e+00 | 31/33 (SW 900, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.300×** | -20.8 | 0e+00 | 30/31 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.369×** | -17.3 | 0e+00 | 26/33 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.392×** | -16.2 | 0e+00 | 27/31 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.434×** | -14.4 | 4e-45 | 27/33 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.494×** | -12.2 | 3e-32 | 25/32 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.639×** | -10.9 | 5e-26 | 19/33 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.590×** | -8.8 | 1e-16 | 19/31 (SW 900, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.615×** | -8.4 | 2e-15 | 24/33 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.660×** | -6.9 | 3e-10 | 17/29 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.661×** | -6.9 | 3e-10 | 18/30 (MIA PaCa-2, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.679×** | -6.7 | 1e-09 | 17/34 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.774×** | -6.3 | 2e-08 | 16/34 (NCI-H2347, SW1417, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.502×** | -6.2 | 2e-08 | 15/32 (HS-578T, J82, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.716×** | -5.8 | 3e-07 | 17/32 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.605×** | -4.5 | 2e-04 | 11/30 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.799×** | -3.9 | 0.003 | 10/32 (A-172, HEC-1-A, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7853. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 27.3 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0852× (z -25.3) |
| [[PANC-1 (line)]] | alt | 21.0 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -24.7) |
| [[LoVo (line)]] | wt | 12.3 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.122× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.248× (z -14.9) |
| [[HEC-1-A (line)]] | alt | 20.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -21.3) |
| [[NCI-H2030 (line)]] | alt | 24.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -18.6) |
| [[NCI-H23 (line)]] | alt | 43.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -18.9) |
| [[NCI-H2347 (line)]] | alt | 11.1 | 1 | 4 | [[Tucidinostat (drug)]] 5 µM 2.76× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -20.3) |
| [[SW 900 (line)]] | alt | 13.9 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0167× (z -21.0) |
| [[A-427 (line)]] | wt | 40.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -22.5) |
| [[HS-578T (line)]] | alt | 19.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -19.7) |
| [[J82 (line)]] | alt | 13.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -16.0) |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -15.9) |
| [[SNU-1 (line)]] | wt | 37.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.221× (z -9.2) |
| [[SW1417 (line)]] | alt | 41.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -21.0) |
| [[HCT15 (line)]] | alt | 25.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -13.9) |
| [[HOP62 (line)]] | alt | 12.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 11.9 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0907× (z -12.5) |
| [[SK-MEL-2 (line)]] | alt | 9.41 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0620× (z -11.6) |
| [[BT-474 (line)]] | alt | 5.08 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0278× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 7.76 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0486× (z -10.4) |
| [[A-172 (line)]] | wt | 6.39 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -11.4) |
| [[A498 (line)]] | wt | 9.16 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.216× (z -9.6) |
| [[A549 (line)]] | wt | 7.28 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -10.7) |
| [[AN3 CA (line)]] | alt | 40.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 45.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 10.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0680× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 3.68 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.28× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 5.60 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0629× (z -10.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 7.70 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -13.1) |
| [[AsPC-1 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.34 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7853), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPT]] | +0.73 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[WASF3]] | +0.73 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[RIMS3]] | +0.72 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[SEPTIN3]] | +0.68 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[SMARCD3]] | +0.68 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[ZNF483]] | +0.67 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[MAP6]] | +0.66 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[TMOD2]] | +0.66 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[ARRB2]] | +0.65 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[KIF1A]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 | pathway: Golgi-to-ER retrograde transport |
| [[GNAZ]] | +0.65 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[PDZD4]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD17-DT]] | -0.61 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[INO80D]] | -0.57 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[WARS2-AS1]] | -0.56 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[HEXIM2-AS1]] | -0.56 | -0.55 / -0.29 | both halves | 3e-04 |  |
| [[LINC01004]] | -0.56 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[MIRLET7IHG]] | -0.56 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[ASH1L]] | -0.56 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[EFCAB2]] | -0.55 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[RFX3-DT]] | -0.55 | -0.57 / -0.22 | both halves | 6e-04 |  |
| [[CHD1-DT]] | -0.55 | -0.55 / -0.26 | both halves | 4e-04 |  |
| [[GTF2IRD2]] | -0.54 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[ERCC6L2]] | -0.54 | -0.51 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 12, C 11. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF26A]] | B | KIF26A activity raises RAB6B's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.46× lower at baseline in the lines without KIF26A | 0.028 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[FSD1]] | B | FSD1 activity raises RAB6B's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 2.43× lower at baseline in the lines without FSD1 | 0.040 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[SCD5]] | B | SCD5 activity raises RAB6B's level | lines that do not express SCD5 (10) vs lines expressing it (40) | 2.78× lower at baseline in the lines without SCD5 | 0.048 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FOXD1, KLF9 |
| [[SCN8A]] | B | SCN8A activity raises RAB6B's level | lines that do not express SCN8A (18) vs lines expressing it (32) | 2.10× lower at baseline in the lines without SCN8A | 0.054 | ⚠ within organs, on part of the lines; also absent: DPYSL5, PDZD4, STOX2 |
| [[LINC00937]] | B | LINC00937 activity raises RAB6B's level | lines that do not express LINC00937 (13) vs lines expressing it (37) | 2.50× lower at baseline in the lines without LINC00937 | 0.064 | ⚠ within organs, on part of the lines; also absent: SYCP2, ENSG00000255367, MRAS; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers RAB6B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers RAB6B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SEMA6B]] | B | SEMA6B activity raises RAB6B's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.24× lower at baseline in the lines without SEMA6B | 0.074 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[GNAZ]] | B | GNAZ activity raises RAB6B's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.49× lower at baseline in the lines without GNAZ | 0.085 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[GJA3]] | B | GJA3 activity raises RAB6B's level | lines that do not express GJA3 (17) vs lines expressing it (33) | 2.13× lower at baseline in the lines without GJA3 | 0.089 | ⚠ within organs, on part of the lines; also absent: GBX1 |
| [[TOP2A]] | B | TOP2A activity raises RAB6B's level | compounds that target TOP2A: 3 of 5 lower it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SNX10]] | B | SNX10 activity raises RAB6B's level | lines that do not express SNX10 (11) vs lines expressing it (39) | 2.47× lower at baseline in the lines without SNX10 | 0.095 | ⚠ within organs, on part of the lines; also absent: AP3B2, LRRC4B, CCDC144CP |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 6, C 9. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNX10]] | B | RAB6B activity raises SNX10's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 2.63× lower at baseline in the lines without RAB6B | 0.015 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS |
| [[SLC46A1]] | B | RAB6B activity raises SLC46A1's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 1.72× lower at baseline in the lines without RAB6B | 0.052 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS |
| [[GJA3]] | B | RAB6B activity raises GJA3's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 2.06× lower at baseline in the lines without RAB6B | 0.053 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS |
| [[MAP3K15]] | B | RAB6B activity raises MAP3K15's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 2.37× lower at baseline in the lines without RAB6B | 0.062 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS |
| [[HOMER2]] | B | RAB6B activity raises HOMER2's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 3.14× lower at baseline in the lines without RAB6B | 0.069 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS |
| [[GAMT]] | B | RAB6B activity raises GAMT's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 1.78× lower at baseline in the lines without RAB6B | 0.099 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS |
| [[TCF7L1]] | C | RAB6B activity raises TCF7L1's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 5.02× lower at baseline in the lines without RAB6B | 0.001 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS; co-absent with the target |
| [[STOX2]] | C | RAB6B activity raises STOX2's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 5.95× lower at baseline in the lines without RAB6B | 0.001 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS; co-absent with the target |
| [[RASGEF1C]] | C | RAB6B activity raises RASGEF1C's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 2.97× lower at baseline in the lines without RAB6B | 0.006 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS; co-absent with the target |
| [[PDZD4]] | C | RAB6B activity raises PDZD4's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 3.50× lower at baseline in the lines without RAB6B | 0.007 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS; co-absent with the target |
| [[FAM124A]] | C | RAB6B activity raises FAM124A's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 2.83× lower at baseline in the lines without RAB6B | 0.017 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS; co-absent with the target |
| [[FBXO27]] | C | RAB6B activity raises FBXO27's level | lines that do not express RAB6B (14) vs lines expressing it (36) | 3.09× lower at baseline in the lines without RAB6B | 0.034 | ⚠ within organs, on part of the lines; also absent: FAM124A, WNT9A, MRAS; co-absent with the target |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.814). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (4.0, 40.6); signed map (-25.3, 34.8). **Vector** length 83.4, 19.4% of its response variance represented; |z| ≥ 3 in 858 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +14.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.2 | +14.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.9 | +8.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +5.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +6.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +2.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -21.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | -35.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -20.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.0 | -12.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -14.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -6.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -0.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | RAB6B, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.1 — chr3:133,824,235-133,895,882 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 10 pathways, smallest: TBC/RABGAPs; COPI-independent Golgi-to-ER retrograde traffic; Retrograde transport at the Trans-Golgi-Network |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRW1](https://www.uniprot.org/uniprotkb/Q9NRW1) (Ras-related protein Rab-6B):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between active GTP-bound and inactive GDP-bound states. In their active state, drive transport of vesicular carriers from donor organelles to acceptor organelles to regulate the membrane traffic that maintains organelle identity and morphology (By similarity). Recruits VPS13B to the Golgi membrane. Regulates the compacted morphology …

**Summary**, from NCBI Gene [51560](https://www.ncbi.nlm.nih.gov/gene/51560):

> Enables G protein activity and myosin V binding activity. Involved in Golgi organization and protein localization to Golgi membrane. Located in Golgi membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14902](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14902) · Entrez [51560](https://www.ncbi.nlm.nih.gov/gene/51560) · UniProt [Q9NRW1](https://www.uniprot.org/uniprotkb/Q9NRW1) · Ensembl [ENSG00000154917](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154917)

## Data

Gene col 7853: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7853); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7853, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7853]; `tensor/DDL_lfc|DDL_z.npy` [7853]; `embed/gene_vectors.npy` [7853]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7853 or target_col == 7853). Every well: [[RAB6B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB6B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
