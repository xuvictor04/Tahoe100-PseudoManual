---
symbol: "ZFAND6"
type: "gene"
col: 1467
ensembl_id: "ENSG00000086666"
name: "zinc finger AN1-type containing 6"
location: "15q25.1"
module: 184
arm: "+"
pooled_cpm: 192.87
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/184"]
generated_by: "tahoemap"
---

# ZFAND6

*zinc finger AN1-type containing 6* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.83× (z +11.9, q 9e-30, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.635× (z -8.6, q 4e-15, down in 33 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.632× (z -4.7, q 2e-04, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPK8]] (+0.60, fdr 1e-05), [[CBL]] (+0.52, fdr 3e-05), [[PTPN12]] (+0.52, fdr 2e-05); moves opposite to [[GTF3C4]] (-0.55, fdr 2e-05), [[PES1]] (-0.54, fdr 2e-05), [[AKAP8]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 184]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MYO1D]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1467.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +11.9 | 9e-30 | 42/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.77×** | +11.3 | 6e-27 | 42/48 (KATO III, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +9.8 | 2e-20 | 45/48 (HS-578T, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.53×** | +8.3 | 1e-14 | 43/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +7.8 | 6e-13 | 35/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +7.5 | 5e-12 | 34/48 (hTERT-HPNE, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +7.5 | 7e-12 | 38/48 (hTERT-HPNE, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +7.3 | 2e-11 | 38/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +5.5 | 3e-06 | 32/47 (LoVo, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +4.6 | 2e-04 | 32/49 (HS-578T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.006 | 24/48 (Hs 766T, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +3.8 | 0.006 | 26/48 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.8 | 0.007 | 21/48 (RKO, NCI-H460, …) | top dose only | composition shift |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 1.20× | +3.4 | 0.032 | 21/48 (SNU-1, H4, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.040 | 23/49 (hTERT-HPNE, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.040 | 25/48 (RKO, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.044 | 18/48 (KATO III, HCT15, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1467.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.635×** | -8.6 | 4e-15 | 33/44 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.666×** | -8.0 | 3e-13 | 37/49 (NCI-H1573, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.717×** | -6.6 | 9e-09 | 34/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.768×** | -5.2 | 2e-05 | 29/48 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.632×** | -4.7 | 2e-04 | 32/48 (NCI-H460, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.666×** | -4.2 | 0.003 | 28/48 (NCI-H2347, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.679×** | -4.0 | 0.005 | 29/48 (NCI-H2347, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.816×** | -3.9 | 0.007 | 24/47 (HepG2/C3A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.875× | -3.8 | 0.011 | 16/48 (SW 900, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **0.701×** | -3.7 | 0.014 | 26/48 (NCI-H2347, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.712×** | -3.5 | 0.024 | 25/48 (NCI-H2347, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.804×** | -3.1 | 0.098 | 23/48 (Hs 766T, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.899× | -3.0 | 0.12 | 2/48 (Hs 766T, hTERT-HPNE) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1467. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 161 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +15.2) | — |
| [[LoVo (line)]] | wt | 239 | 6 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -15.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 155 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.590× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 361 | 3 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 134 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.503× (z -10.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 238 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.82× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.458× (z -9.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 188 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 224 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.34× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.410× (z -10.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 109 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.47× (z +12.3) | — |
| [[A498 (line)]] | wt | 187 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.22× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 93.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.87× (z +12.7) | — |
| [[hTERT-HPNE (line)]] | wt | 117 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.46× (z +12.6) | — |
| [[NCI-H2347 (line)]] | alt | 316 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.386× (z -13.6) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 209 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.388× (z -9.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 151 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 1.67× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 255 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +12.7) | [[Docetaxel (drug)]] 0.05 µM 0.592× (z -8.5) ⚠ transcription drop |
| [[SNU-423 (line)]] | alt | 121 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.19× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 252 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -12.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 135 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 109 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.41× (z +10.0) | — |
| [[A549 (line)]] | wt | 348 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -10.0) ⚠ cell-cycle shift, explains ~3% of this change |
| [[CFPAC-1 (line)]] | alt | 182 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.89× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 203 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 158 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.381× (z -12.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 106 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.50× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 229 | 1 | 0 | [[Digitoxin (drug)]] 0.5 µM 2.33× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 214 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 194 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.268× (z -8.8) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 225 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.66× (z +8.6) | — |
| [[RKO (line)]] | wt | 188 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +13.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RPMI-7951 (line)]] | alt | 248 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.485× (z -8.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 161 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -17.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 166 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.376× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 301 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -10.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 199 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.613× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 169 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.358× (z -8.7) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 232 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 211 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 168 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 186 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 166 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 184 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 123 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1467), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK8]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[CBL]] | +0.52 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[PTPN12]] | +0.52 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[AMN1]] | +0.51 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[PARD3]] | +0.51 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[ORMDL2]] | +0.51 | +0.49 / +0.43 | both halves | 4e-05 |  |
| [[RASA2]] | +0.50 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[SGPP1]] | +0.50 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[ITGB5]] | +0.50 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[ARPC1B]] | +0.50 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[RICTOR]] | +0.49 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[FAM3C]] | +0.48 | +0.51 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*59 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF3C4]] | -0.55 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[PES1]] | -0.54 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[AKAP8]] | -0.54 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[FASTKD2]] | -0.53 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[NOL8]] | -0.51 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[MCPH1]] | -0.51 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[GATB]] | -0.51 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[GTF2H1]] | -0.49 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[MTRF1]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[TACO1]] | -0.49 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[AIMP1]] | -0.49 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[MIX23]] | -0.49 | -0.43 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO1D]] | B | MYO1D activity raises ZFAND6's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 1.38× lower at baseline in the lines without MYO1D | 0.078 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 184]]; 20 genes; this gene is in the **+** arm (projection on the module's main direction 0.471). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-37.8, 11.9); signed map (41.3, -31.9). **Vector** length 119, 42.0% of its response variance represented; |z| ≥ 3 in 1,215 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.8 | +7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.8 | +4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.0 | +9.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.2 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | -8.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.6 | +0.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.3 | -0.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | -0.9 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -9.2 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.6 | -6.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.0 | +0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.9 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -0.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.0 | -4.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.9 | -4.0 |
|  | [[EX229 (drug)]] 5 µM |  | -4.9 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.5 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger AN1-type containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:80,059,568-80,138,393 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZFAND5B, AWP1; previously ZA20D3 |
| Gene groups (HGNC) | Zinc fingers AN1-type; Zinc fingers A20-type |
| Reactome | 2 pathways, smallest: Peroxisomal protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6FIF0](https://www.uniprot.org/uniprotkb/Q6FIF0) (AN1-type zinc finger protein 6):

> Involved in regulation of TNF induced NF-kappa-B activation and apoptosis. Involved in modulation of 'Lys-48'-linked polyubiquitination status of TRAF2 and decreases association of TRAF2 with RIPK1. Required for PTS1 target sequence-dependent protein import into peroxisomes and PEX5 stability; may cooperate with PEX6. In vitro involved in PEX5 export from the cytosol to peroxisomes (By similarity).

**Summary**, from NCBI Gene [54469](https://www.ncbi.nlm.nih.gov/gene/54469):

> Predicted to enable polyubiquitin modification-dependent protein binding activity. Involved in cellular response to tumor necrosis factor; negative regulation of apoptotic process; and regulation of canonical NF-kappaB signal transduction. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30164](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30164) · Entrez [54469](https://www.ncbi.nlm.nih.gov/gene/54469) · UniProt [Q6FIF0](https://www.uniprot.org/uniprotkb/Q6FIF0) · Ensembl [ENSG00000086666](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086666)

## Data

Gene col 1467: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1467); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1467, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1467]; `tensor/DDL_lfc|DDL_z.npy` [1467]; `embed/gene_vectors.npy` [1467]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1467 or target_col == 1467). Every well: [[ZFAND6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFAND6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
