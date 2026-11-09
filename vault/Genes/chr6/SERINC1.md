---
symbol: "SERINC1"
type: "gene"
col: 3303
ensembl_id: "ENSG00000111897"
name: "serine incorporator 1"
location: "6q22.31"
module: 69
arm: "+"
pooled_cpm: 166.87
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# SERINC1

*serine incorporator 1* — 6q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.24× (z +9.6, q 5e-19, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.417× (z -19.8, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[venetoclax (drug)]] 5 µM: 0.438× (z -9.7, q 5e-20, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBXN7]] (+0.76, fdr 7e-06), [[TMEM59]] (+0.72, fdr 7e-06), [[TCP11L2]] (+0.70, fdr 7e-06); moves opposite to [[NAA15]] (-0.58, fdr 1e-05), [[CEP83]] (-0.58, fdr 1e-05), [[TCERG1]] (-0.56, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MFGE8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3303.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.24×** | +9.6 | 5e-19 | 44/49 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +9.2 | 1e-17 | 37/48 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +6.5 | 2e-08 | 29/48 (BT-474, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.66×** | +6.0 | 3e-07 | 33/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +5.7 | 1e-06 | 29/48 (BT-474, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +5.2 | 2e-05 | 28/48 (NCI-H1573, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.5 | 5e-04 | 20/49 (MIA PaCa-2, AsPC-1, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.41×** | +4.1 | 0.003 | 31/47 (C32, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +3.6 | 0.018 | 20/49 (HS-578T, COLO 205, …) | all doses, flat | composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.020 | 23/48 (PANC-1, LoVo, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.4 | 0.030 | 20/50 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | 1.16× | +3.4 | 0.030 | 19/48 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.2 | 0.066 | 10/48 (HEC-1-A, J82, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3303.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.417×** | -19.8 | 0e+00 | 48/48 (NCI-H2347, MIA PaCa-2, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.438×** | -9.7 | 5e-20 | 48/48 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.454×** | -9.3 | 2e-18 | 48/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.484×** | -8.6 | 1e-15 | 44/48 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.485×** | -8.5 | 1e-15 | 46/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.490×** | -8.4 | 3e-15 | 46/48 (PANC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.659×** | -6.7 | 2e-09 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.757×** | -6.0 | 1e-07 | 33/49 (HepG2/C3A, hTERT-HPNE, …) | top dose only |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.776×** | -5.7 | 8e-07 | 40/49 (PANC-1, AsPC-1, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.734×** | -5.0 | 4e-05 | 35/49 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.819×** | -4.2 | 0.001 | 27/48 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.778×** | -4.0 | 0.003 | 24/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | 0.846× | -3.6 | 0.014 | 21/47 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.852× | -3.4 | 0.023 | 12/49 (RKO, LoVo, …) | top dose only | plate-row cell shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.857× | -3.4 | 0.023 | 15/48 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Afatinib (drug)]] 0.5 µM |  | 0.900× | -3.1 | 0.057 | 4/49 (LS 180, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **0.828×** | -3.0 | 0.075 | 18/48 (PANC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3303. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 216 | 1 | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.72× (z +10.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.396× (z -17.4) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.355× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 203 | 0 | 5 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.399× (z -14.4) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 109 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +11.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.419× (z -11.9) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 162 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +11.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.465× (z -9.7) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 107 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +12.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.455× (z -9.8) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 156 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.86× (z +11.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.426× (z -13.2) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 136 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.49× (z +9.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.450× (z -11.5) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 186 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.313× (z -19.8) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.365× (z -9.0) |
| [[A549 (line)]] | wt | 158 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.351× (z -15.0) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.318× (z -8.6) |
| [[AN3 CA (line)]] | alt | 195 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -16.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 221 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +12.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.364× (z -15.4) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 229 | 0 | 2 (1 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.419× (z -10.9) |
| [[HS-578T (line)]] | alt | 182 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.93× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.387× (z -12.7) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 177 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +11.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.379× (z -13.2) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 190 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.253× (z -17.4) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.270× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 203 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +9.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.415× (z -10.8) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 103 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +10.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.300× (z -16.9) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 163 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.476× (z -10.1) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 129 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.471× (z -10.6) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.380× (z -9.6) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 153 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.438× (z -9.7) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 125 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.372× (z -9.4) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 192 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.426× (z -10.3) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 168 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.317× (z -16.7) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 165 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.408× (z -12.5) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 158 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.463× (z -9.9) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 250 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.431× (z -11.7) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 216 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.353× (z -16.4) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 179 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.431× (z -11.2) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.354× (z -12.4) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.446× (z -10.2) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 134 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.313× (z -12.7) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 210 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.424× (z -11.4) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.457× (z -9.6) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 202 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.479× (z -9.5) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 172 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.246× (z -15.0) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 296 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.511× (z -9.8) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 190 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.492× (z -9.9) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.333× (z -14.7) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 134 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.288× (z -11.7) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 188 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 222 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3303), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBXN7]] | +0.76 | +0.64 / +0.80 | both halves | 7e-06 |  |
| [[TMEM59]] | +0.72 | +0.58 / +0.78 | both halves | 7e-06 |  |
| [[TCP11L2]] | +0.70 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[CCDC28A]] | +0.70 | +0.62 / +0.81 | both halves | 7e-06 |  |
| [[YPEL5]] | +0.70 | +0.54 / +0.80 | both halves | 1e-05 | STRING 437 |
| [[SLU7]] | +0.69 | +0.38 / +0.76 | both halves | 6e-05 |  |
| [[MKRN1]] | +0.69 | +0.58 / +0.77 | both halves | 7e-06 |  |
| [[HBP1]] | +0.69 | +0.52 / +0.78 | both halves | 1e-05 |  |
| [[SERINC3]] | +0.68 | +0.56 / +0.77 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives |
| [[RB1CC1]] | +0.68 | +0.45 / +0.76 | both halves | 3e-05 |  |
| [[CREBRF]] | +0.67 | +0.41 / +0.78 | both halves | 4e-05 |  |
| [[CALCOCO1]] | +0.67 | +0.59 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA15]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[CEP83]] | -0.58 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[TCERG1]] | -0.56 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[PUS1]] | -0.56 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[ZNG1F]] | -0.55 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[RAD51D]] | -0.55 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[HEATR3]] | -0.55 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[WDR4]] | -0.54 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[PDSS1]] | -0.54 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[CLN6]] | -0.54 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[UQCC2]] | -0.53 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[ZNRF3]] | -0.53 | -0.54 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MFGE8]] | B | MFGE8 activity raises SERINC1's level | lines that do not express MFGE8 (7) vs lines expressing it (43) | 1.27× lower at baseline in the lines without MFGE8 | 0.023 | ⚠ within organs, on part of the lines; also absent: P3H1, HAPLN3, FAM171B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.781). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.1, -44.5); signed map (-14.5, 10.2). **Vector** length 138, 45.9% of its response variance represented; |z| ≥ 3 in 1,115 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.3 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.2 | +4.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +4.7 | +3.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +0.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.8 | +0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.5 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -18.8 | -19.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -11.4 | -8.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -10.8 | -9.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -10.6 | -8.5 |
|  | [[EX229 (drug)]] 5 µM |  | -10.3 | -8.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -10.2 | -9.7 |

## What is on record

|  |  |
|---|---|
| Name | serine incorporator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.31 — chr6:122,443,351-122,471,807 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TMS-2, TDE1L, KIAA1253; previously TDE2 |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 2 pathways, smallest: Serine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRX5](https://www.uniprot.org/uniprotkb/Q9NRX5) (Serine incorporator 1):

> Enhances the incorporation of serine into phosphatidylserine and sphingolipids.

**Summary**, from NCBI Gene [57515](https://www.ncbi.nlm.nih.gov/gene/57515):

> Predicted to enable acetyltransferase activator activity; enzyme binding activity; and protein-macromolecule adaptor activity. Predicted to be involved in membrane biogenesis; phosphatidylserine metabolic process; and sphingolipid metabolic process. Predicted to be located in endoplasmic reticulum membrane and plasma membrane. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13464](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13464) · Entrez [57515](https://www.ncbi.nlm.nih.gov/gene/57515) · UniProt [Q9NRX5](https://www.uniprot.org/uniprotkb/Q9NRX5) · Ensembl [ENSG00000111897](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111897)

## Data

Gene col 3303: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3303); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3303, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3303]; `tensor/DDL_lfc|DDL_z.npy` [3303]; `embed/gene_vectors.npy` [3303]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3303 or target_col == 3303). Every well: [[SERINC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERINC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
