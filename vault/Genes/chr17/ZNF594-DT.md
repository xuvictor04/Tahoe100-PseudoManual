---
symbol: "ZNF594-DT"
type: "gene"
col: 15374
ensembl_id: "ENSG00000261879"
name: "ZNF594 divergent transcript"
location: "17p13.2"
module: 209
arm: "+"
pooled_cpm: 11.34
n_lines_expressing: 43
n_dd_up: 16
n_dd_down: 26
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 22
tags: ["gene", "module/209"]
generated_by: "tahoemap"
---

# ZNF594-DT

*ZNF594 divergent transcript* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.60× (z +6.0, q 9e-07, up in 27 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.574× (z -10.0, q 1e-20, down in 25 of 40 measured lines) ⚠ cell-cycle shift, explains ~59% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.596× (z -9.3, q 3e-18, down in 27 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF461]] (+0.70, fdr 1e-05), [[NISCH]] (+0.66, fdr 1e-05), [[MORN4]] (+0.65, fdr 8e-06); moves opposite to [[DGKH]] (-0.50, fdr 5e-05), [[SCHIP1]] (-0.50, fdr 2e-05), [[ATP11C]] (-0.49, fdr 6e-05).
> It is in [[Module 209]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ITPR2]] → it (grade B ⚠); 22 go from it, the strongest it → [[TMEM143]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15374.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.60×** | +6.0 | 9e-07 | 27/41 (SW480, NCI-H23, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +5.1 | 1e-04 | 19/36 (SW480, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.31×** | +4.9 | 2e-04 | 17/41 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.49×** | +4.6 | 5e-04 | 17/41 (LS 180, PANC-1, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.006 | 8/41 (HEC-1-A, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.019 | 11/41 (SW480, HEC-1-A, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.49×** | +3.7 | 0.020 | 9/36 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.021 | 9/41 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.32×** | +3.5 | 0.028 | 13/41 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.030 | 9/41 (A-172, BT-474, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.038 | 13/41 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.040 | 15/41 (LS 180, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.040 | 10/41 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.3 | 0.040 | 13/40 (NCI-H1792, SNU-1, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.35×** | +3.2 | 0.051 | 8/41 (SW480, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +3.2 | 0.051 | 11/41 (NCI-H23, SHP-77, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15374.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.574×** | -10.0 | 1e-20 | 25/40 (SNU-423, A498, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.454×** | -9.6 | 2e-19 | 30/36 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.596×** | -9.3 | 3e-18 | 27/40 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.485×** | -9.2 | 5e-18 | 32/41 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.539×** | -7.8 | 5e-13 | 24/38 (NCI-H460, SNU-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.521×** | -7.5 | 7e-12 | 23/40 (SW480, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.560×** | -7.1 | 1e-10 | 22/40 (SNU-423, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.586×** | -6.8 | 8e-10 | 20/39 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.612×** | -6.2 | 3e-08 | 22/40 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.408×** | -6.0 | 1e-07 | 24/41 (A-172, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.630×** | -5.9 | 2e-07 | 22/40 (SW480, A-172, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.633×** | -5.8 | 3e-07 | 23/41 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.635×** | -5.8 | 4e-07 | 20/41 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **0.675×** | -5.0 | 2e-05 | 17/31 (NCI-H23, HS-578T, …) | inconsistent across doses | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.475×** | -4.9 | 3e-05 | 13/36 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.700×** | -4.5 | 2e-04 | 13/40 (SNU-423, MIA PaCa-2, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.681×** | -4.4 | 3e-04 | 16/41 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.528×** | -4.2 | 6e-04 | 17/40 (A498, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.730×** | -3.8 | 0.004 | 18/40 (HT-29, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.577×** | -3.7 | 0.006 | 12/37 (MIA PaCa-2, C32, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.835× | -3.2 | 0.030 | 10/41 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.779×** | -3.0 | 0.049 | 13/40 (A549, NCI-H661, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15374. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.5 | 0 | 8 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.240× (z -10.3) |
| [[SW480 (line)]] | alt | 21.6 | 0 | 7 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.215× (z -14.0) |
| [[A-172 (line)]] | wt | 21.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -16.5) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.191× (z -11.5) |
| [[A498 (line)]] | wt | 18.3 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -17.3) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.237× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 22.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -14.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.156× (z -11.7) |
| [[HS-578T (line)]] | alt | 17.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -10.8) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -9.1) |
| [[SNU-1 (line)]] | wt | 18.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0796× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.127× (z -9.4) |
| [[A-427 (line)]] | wt | 13.8 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0881× (z -14.0) ⚠ cell-cycle shift, explains ~17% of this change |
| [[NCI-H23 (line)]] | alt | 30.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 15.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0750× (z -20.9) ⚠ cell-cycle shift, explains ~59% of this change |
| [[C32 (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -8.7) ⚠ cell-cycle shift, explains ~20% of this change |
| [[H4 (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0567× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 8.12 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.134× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.111× (z -8.6) |
| [[J82 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.147× (z -10.6) ⚠ cell-cycle shift, explains ~48% of this change |
| [[PANC-1 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -12.4) ⚠ cell-cycle shift, explains ~59% of this change |
| [[A549 (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15374), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF461]] | +0.70 | +0.50 / +0.79 | both halves | 1e-05 |  |
| [[NISCH]] | +0.66 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[MORN4]] | +0.65 | +0.58 / +0.72 | both halves | 8e-06 |  |
| [[ZNF559]] | +0.65 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[DYNC2LI1]] | +0.64 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[ZNF559-ZNF177]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[ZNF573]] | +0.63 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[SETDB1]] | +0.62 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[GUSBP2-1]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[USP30]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ASTE1]] | +0.60 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[ZNF552]] | +0.60 | +0.46 / +0.69 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGKH]] | -0.50 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[SCHIP1]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ATP11C]] | -0.49 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[PRKCA]] | -0.49 | -0.43 / -0.54 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITPR2]] | B | ITPR2 activity raises ZNF594-DT's level | lines that do not express ITPR2 (5) vs lines expressing it (45) | 1.68× lower at baseline in the lines without ITPR2 | 0.088 | ⚠ within organs, on part of the lines; also absent: ITPR2-AS1, ENSG00000286162, SPATA17; maybe low, not absent |
| [[FAM182B]] | C | FAM182B activity raises ZNF594-DT's level | lines that do not express FAM182B (4) vs lines expressing it (46) | 1.94× lower at baseline in the lines without FAM182B | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CATSPER2P1, FGF12, SLFNL1-AS1; maybe low, not absent; its own permutation p |
| [[SIPA1L2]] | C | SIPA1L2 activity raises ZNF594-DT's level | lines that do not express SIPA1L2 (10) vs lines expressing it (40) | 2.20× lower at baseline in the lines without SIPA1L2 | 0.072 | ⚠ within organs, on part of the lines; also absent: ZNF594-DT, LINC02036, MGC4859; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 21, C 1. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM143]] | B | ZNF594-DT activity raises TMEM143's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without ZNF594-DT | 0.002 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[YJU2B]] | B | ZNF594-DT activity raises YJU2B's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.50× lower at baseline in the lines without ZNF594-DT | 0.007 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[ATP6V0D1-DT]] | B | ZNF594-DT activity raises ATP6V0D1-DT's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.77× lower at baseline in the lines without ZNF594-DT | 0.009 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[TTLL1]] | B | ZNF594-DT activity raises TTLL1's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.61× lower at baseline in the lines without ZNF594-DT | 0.012 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[TAB1]] | B | ZNF594-DT activity raises TAB1's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.39× lower at baseline in the lines without ZNF594-DT | 0.017 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[ZNF500]] | B | ZNF594-DT activity raises ZNF500's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.30× lower at baseline in the lines without ZNF594-DT | 0.028 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[TMEM254]] | B | ZNF594-DT activity raises TMEM254's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.68× lower at baseline in the lines without ZNF594-DT | 0.031 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[DYNC2LI1]] | B | ZNF594-DT activity raises DYNC2LI1's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without ZNF594-DT | 0.032 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[FAM182B]] | B | ZNF594-DT activity raises FAM182B's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.62× lower at baseline in the lines without ZNF594-DT | 0.032 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[D2HGDH]] | B | ZNF594-DT activity strengthens D2HGDH's drug response | lines that do not express ZNF594-DT (7) vs lines expressing it (41) | the lines without ZNF594-DT respond 0.59× as strongly (z diff +2.45); strongest at Digitoxin 5 µM: 0.66x vs 0.24x (z diff +4.6) | 0.032 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1; target measured in part of the lines; artifact flags |
| [[STAG3L4-1]] | B | ZNF594-DT activity raises STAG3L4-1's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.50× lower at baseline in the lines without ZNF594-DT | 0.036 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[NPHP1]] | B | ZNF594-DT activity raises NPHP1's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 2.18× lower at baseline in the lines without ZNF594-DT | 0.037 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |

## Where it sits

- **Module**: [[Module 209]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-30.0, -4.5); signed map (-16.6, -16.6). **Vector** length 69.1, 12.8% of its response variance represented; |z| ≥ 3 in 928 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.9 | +5.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | +3.8 | +4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +6.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | +2.5 | +3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +3.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -9.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -4.0 | -3.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.4 | -9.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -2.9 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -5.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ZNF594 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17p13.2 — chr17:5,192,007-5,248,182 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55347](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55347) · Entrez [100130950](https://www.ncbi.nlm.nih.gov/gene/100130950) · Ensembl [ENSG00000261879](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000261879)

## Data

Gene col 15374: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15374); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15374, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15374]; `tensor/DDL_lfc|DDL_z.npy` [15374]; `embed/gene_vectors.npy` [15374]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15374 or target_col == 15374). Every well: [[ZNF594-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF594-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
