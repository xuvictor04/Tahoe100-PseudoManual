---
symbol: "GDI2"
type: "gene"
col: 648
ensembl_id: "ENSG00000057608"
name: "GDP dissociation inhibitor 2"
location: "10p15.1"
module: 42
arm: "+"
pooled_cpm: 212.14
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 4
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# GDI2

*GDP dissociation inhibitor 2* — 10p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.48× (z +10.9, q 7e-25, up in 32 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 1.27× (z +6.6, q 7e-09, up in 28 of 50 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.765× (z -10.9, q 6e-25, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGA3]] (+0.70, fdr 7e-06), [[NDEL1]] (+0.66, fdr 7e-06), [[TPP2]] (+0.64, fdr 7e-06); moves opposite to [[RAB9A]] (-0.60, fdr 1e-05), [[PAFAH2]] (-0.57, fdr 1e-04), [[ZSCAN18]] (-0.57, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TLCD5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 648.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +10.9 | 7e-25 | 32/44 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +9.9 | 1e-20 | 35/49 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +6.6 | 7e-09 | 28/50 (MIA PaCa-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +5.0 | 9e-05 | 24/48 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +4.9 | 1e-04 | 0/50 | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.35×** | +4.5 | 7e-04 | 28/48 (NCI-H460, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.007 | 21/48 (NCI-H1792, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.8 | 0.010 | 22/45 (Hs 766T, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.14× | +3.7 | 0.016 | 19/48 (SW48, RKO, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | 1.14× | +3.6 | 0.018 | 16/47 (SK-MEL-2, Panc 03.27, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.08× | +3.2 | 0.073 | 1/49 (NCI-H1792) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 648.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.765×** | -10.9 | 6e-25 | 30/48 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.776×** | -7.3 | 8e-11 | 31/48 (hTERT-HPNE, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.856× | -6.3 | 4e-08 | 19/48 (NCI-H2347, SW 900, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.827×** | -5.5 | 6e-06 | 24/48 (NCI-H2030, hTERT-HPNE, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.705×** | -5.3 | 2e-05 | 31/49 (NCI-H2030, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.887× | -4.9 | 9e-05 | 11/48 (LOX-IMVI, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.845× | -4.9 | 9e-05 | 20/49 (HT-29, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.838× | -4.8 | 1e-04 | 22/47 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.850× | -4.7 | 2e-04 | 21/48 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.842× | -4.6 | 2e-04 | 18/47 (A-172, C-33 A, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.848× | -4.6 | 2e-04 | 19/47 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.851× | -4.6 | 2e-04 | 18/48 (HCT15, LoVo, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.864× | -4.2 | 0.001 | 14/48 (hTERT-HPNE, RKO, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.869× | -4.1 | 0.002 | 10/48 (HS-578T, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.866× | -4.0 | 0.003 | 21/47 (HOP62, SW1417, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.902× | -3.4 | 0.016 | 4/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.890× | -3.4 | 0.019 | 8/48 (HOP62, J82, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.892× | -3.3 | 0.028 | 3/48 (SW48, A-172, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.930× | -2.9 | 0.085 | 1/49 (SW480) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 648. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 254 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -17.2) |
| [[HOP62 (line)]] | alt | 215 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.601× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 237 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.95× (z +15.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 191 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.94× (z +14.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 278 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -24.8) |
| [[A549 (line)]] | wt | 283 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +13.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 200 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 1.81× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -14.0) |
| [[HT-29 (line)]] | alt | 236 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.05× (z +11.9) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 263 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -15.1) |
| [[J82 (line)]] | alt | 232 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -14.5) |
| [[NCI-H1792 (line)]] | alt | 292 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +13.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 175 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.86× (z +11.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 159 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.36× (z +14.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 202 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.22× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 265 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -17.4) |
| [[SW48 (line)]] | wt | 217 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +9.8) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.484× (z -9.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 229 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +13.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 191 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -17.0) |
| [[C-33 A (line)]] | alt | 186 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.508× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~20% of this change |
| [[H4 (line)]] | wt | 202 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.563× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 227 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.642× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 98.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.49× (z +11.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 230 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -18.0) |
| [[NCI-H23 (line)]] | alt | 216 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -12.4) |
| [[PANC-1 (line)]] | alt | 161 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.56× (z +9.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 329 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.536× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[RPMI-7951 (line)]] | alt | 241 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.523× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 181 | 0 | 1 | — | [[Fluvoxamine (drug)]] 0.05 µM 0.141× (z -9.4) |
| [[SW1417 (line)]] | alt | 242 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.631× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 226 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 316 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 78.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 189 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 200 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 316 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 152 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 180 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 255 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 244 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 170 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 648), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA3]] | +0.70 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[NDEL1]] | +0.66 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[TPP2]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[DDB1]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[RECQL]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[TMED3]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[RARS2]] | +0.62 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[PPIP5K2]] | +0.61 | +0.49 / +0.73 | both halves | 1e-05 |  |
| [[HDLBP]] | +0.61 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[TXNDC5]] | +0.60 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[PMM2]] | +0.60 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[COPG1]] | +0.60 | +0.61 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB9A]] | -0.60 | -0.51 / -0.61 | both halves | 1e-05 | pathway: RAB GEFs exchange GTP for GDP on RABs; STRING 915 |
| [[PAFAH2]] | -0.57 | -0.71 / -0.33 | both halves | 1e-04 |  |
| [[ZSCAN18]] | -0.57 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[SPPL3]] | -0.57 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[KAT6A]] | -0.56 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[COIL]] | -0.55 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[MTMR3]] | -0.53 | -0.37 / -0.48 | both halves | 7e-05 |  |
| [[LIPT1]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[ZFHX2]] | -0.52 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[WBP4]] | -0.52 | -0.60 / -0.38 | both halves | 7e-05 |  |
| [[MARK2]] | -0.52 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[EID2]] | -0.52 | -0.55 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLCD5]] | B | TLCD5 activity raises GDI2's level | lines that do not express TLCD5 (5) vs lines expressing it (45) | 1.23× lower at baseline in the lines without TLCD5 | 0.089 | ⚠ within organs, on part of the lines; also absent: DNAJB5, SYDE2, CEP170; maybe low, not absent |
| [[P3H1]] | C | P3H1 activity raises GDI2's level | lines that do not express P3H1 (4) vs lines expressing it (46) | 1.23× lower at baseline in the lines without P3H1 | 0.045 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEP112, TIMP2, CNTNAP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.637). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.9, -28.1); signed map (-53.2, 4.5). **Vector** length 131, 39.6% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.8 | +5.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +4.6 | +3.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.8 | +3.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.6 | +4.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.8 | +2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.8 | +2.3 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.2 | -7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -6.8 | -4.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.4 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.1 | -3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.1 | -10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -6.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.5 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | GDP dissociation inhibitor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.1 — chr10:5,765,223-5,842,132 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RABGDIB |
| Reactome | 6 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P50395](https://www.uniprot.org/uniprotkb/P50395) (Rab GDP dissociation inhibitor beta):

> GDP-dissociation inhibitor preventing the GDP to GTP exchange of most Rab proteins. By keeping these small GTPases in their inactive GDP-bound form regulates intracellular membrane trafficking. Negatively regulates protein transport to the cilium and ciliogenesis through the inhibition of RAB8A.

**Summary**, from NCBI Gene [2665](https://www.ncbi.nlm.nih.gov/gene/2665):

> GDP dissociation inhibitors are proteins that regulate the GDP-GTP exchange reaction of members of the rab family, small GTP-binding proteins of the ras superfamily, that are involved in vesicular trafficking of molecules between cellular organelles. GDIs slow the rate of dissociation of GDP from rab proteins and release GDP from membrane-bound rabs. GDI2 is ubiquitously expressed. The GDI2 gene contains many repetitive elements indicating that it may be prone to inversion/deletion …

**Accessions** — [HGNC:4227](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4227) · Entrez [2665](https://www.ncbi.nlm.nih.gov/gene/2665) · UniProt [P50395](https://www.uniprot.org/uniprotkb/P50395) · Ensembl [ENSG00000057608](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000057608)

## Data

Gene col 648: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 648); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 648, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 648]; `tensor/DDL_lfc|DDL_z.npy` [648]; `embed/gene_vectors.npy` [648]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 648 or target_col == 648). Every well: [[GDI2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GDI2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
