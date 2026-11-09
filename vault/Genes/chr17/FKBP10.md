---
symbol: "FKBP10"
type: "gene"
col: 6573
ensembl_id: "ENSG00000141756"
name: "FKBP prolyl isomerase 10"
location: "17q21.2"
module: 42
arm: "+"
pooled_cpm: 76.52
n_lines_expressing: 40
n_dd_up: 10
n_dd_down: 25
n_dd_up_clean: 5
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 2
direction_downstream: 8
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# FKBP10

*FKBP prolyl isomerase 10* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.90× (z +11.7, q 7e-29, up in 33 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[EX229 (drug)]] 0.5 µM: 1.31× (z +3.5, q 0.044, up in 16 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.223× (z -37.9, q 0e+00, down in 38 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[P3H1]] (+0.72, fdr 7e-06), [[P3H3]] (+0.66, fdr 7e-06), [[PDIA4]] (+0.66, fdr 8e-06); moves opposite to [[DDX52]] (-0.58, fdr 1e-05), [[ERCC4]] (-0.58, fdr 1e-05), [[NSMCE3]] (-0.57, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[P3H3]] → it (grade B ⚠); 8 go from it, the strongest it → [[POGLUT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6573.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.90×** | +11.7 | 7e-29 | 33/39 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +8.8 | 5e-16 | 24/35 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.34×** | +4.9 | 2e-04 | 18/36 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +4.3 | 0.003 | 19/38 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.7 | 0.029 | 16/35 (HepG2/C3A, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.044 | 16/38 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.051 | 12/38 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Pimitespib (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.072 | 17/38 (KATO III, A498, …) | top dose only | noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.072 | 13/38 (A-427, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.083 | 16/38 (Hs 766T, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Salicylic acid (drug)]] 5 µM |  | 1.13× | +3.1 | 0.096 | 4/39 (H4, NCI-H1573, …) | top dose only | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.096 | 7/39 (H4, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6573.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.223×** | -37.9 | 0e+00 | 38/38 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.305×** | -21.7 | 0e+00 | 37/38 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.397×** | -16.3 | 0e+00 | 36/38 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.515×** | -12.2 | 5e-32 | 33/38 (RPMI-7951, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.515×** | -12.2 | 5e-32 | 38/38 (HS-578T, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.556×** | -10.8 | 5e-25 | 33/38 (HS-578T, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.570×** | -10.3 | 5e-23 | 29/38 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.597×** | -9.5 | 2e-19 | 31/38 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.656×** | -7.3 | 2e-11 | 31/38 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.754×** | -7.2 | 4e-11 | 23/38 (CHP-212, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.703×** | -6.2 | 3e-08 | 24/37 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.741×** | -5.5 | 2e-06 | 25/38 (KATO III, H4, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.748×** | -5.3 | 4e-06 | 24/38 (H4, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.774×** | -4.7 | 1e-04 | 22/38 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.776×** | -4.7 | 1e-04 | 21/38 (CHP-212, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.779×** | -4.6 | 2e-04 | 25/38 (HS-578T, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6573. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 168 | 0 | 9 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0314× (z -31.4) |
| [[RPMI-7951 (line)]] | alt | 153 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -30.0) |
| [[HS-578T (line)]] | alt | 201 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -27.8) |
| [[NCI-H460 (line)]] | wt | 121 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -27.5) |
| [[hTERT-HPNE (line)]] | wt | 186 | 0 | 6 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -17.1) |
| [[MIA PaCa-2 (line)]] | alt | 152 | 0 | 6 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0221× (z -44.7) |
| [[NCI-H1573 (line)]] | alt | 31.9 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 4.58× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0831× (z -26.4) |
| [[A498 (line)]] | wt | 178 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -23.8) |
| [[HEC-1-A (line)]] | alt | 77.0 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -18.3) |
| [[KATO III (line)]] | alt | 43.4 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 3.20× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0976× (z -28.3) |
| [[NCI-H2030 (line)]] | alt | 187 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -36.2) |
| [[Hs 766T (line)]] | wt | 97.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -20.7) |
| [[LOX-IMVI (line)]] | wt | 66.9 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -27.9) |
| [[RKO (line)]] | wt | 129 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -11.8) |
| [[SW480 (line)]] | alt | 57.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -22.9) |
| [[A-172 (line)]] | wt | 120 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.41× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -11.6) |
| [[A-427 (line)]] | wt | 82.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -19.3) |
| [[A549 (line)]] | wt | 51.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -17.2) |
| [[CFPAC-1 (line)]] | alt | 36.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -16.6) |
| [[CHP-212 (line)]] | wt | 239 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -16.4) |
| [[HOP62 (line)]] | alt | 58.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -23.7) |
| [[NCI-H2347 (line)]] | alt | 61.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -22.0) |
| [[Panc 03.27 (line)]] | alt | 42.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -19.1) |
| [[PANC-1 (line)]] | alt | 98.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -23.9) |
| [[AN3 CA (line)]] | alt | 110 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -18.0) |
| [[C-33 A (line)]] | alt | 92.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -10.9) |
| [[C32 (line)]] | wt | 35.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.55× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -12.3) |
| [[H4 (line)]] | wt | 162 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -14.7) |
| [[HCT15 (line)]] | alt | 28.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.84× (z +9.1) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.173× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 113 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -12.9) |
| [[NCI-H23 (line)]] | alt | 77.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -17.3) |
| [[SW 900 (line)]] | alt | 57.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -22.3) |
| [[SW48 (line)]] | wt | 54.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -14.4) |
| [[SHP-77 (line)]] | alt | 45.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -13.0) |
| [[SW 1088 (line)]] | alt | 198 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -11.0) |
| [[SW 1271 (line)]] | alt | 108 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 5.72 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.70 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.34 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.9 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.29 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.85 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.91 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.18 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 9.17 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6573), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P3H1]] | +0.72 | +0.72 / +0.69 | both halves | 7e-06 | STRING 866 |
| [[P3H3]] | +0.66 | +0.67 / +0.61 | both halves | 7e-06 | STRING 450 |
| [[PDIA4]] | +0.66 | +0.69 / +0.58 | both halves | 8e-06 | STRING 419 |
| [[PDIA6]] | +0.66 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[MOGS]] | +0.65 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[GANAB]] | +0.64 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[P4HB]] | +0.64 | +0.64 / +0.66 | both halves | 7e-06 | STRING 571 |
| [[CALU]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 | STRING 531 |
| [[PLOD1]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 | STRING 535 |
| [[COLGALT1]] | +0.63 | +0.58 / +0.59 | both halves | 7e-06 | STRING 404 |
| [[DDB1]] | +0.62 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[SEC61A1]] | +0.61 | +0.60 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX52]] | -0.58 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[ERCC4]] | -0.58 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[NSMCE3]] | -0.57 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[TOPORS]] | -0.56 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[MRFAP1L1]] | -0.55 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[NIPBL]] | -0.54 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[C7orf25]] | -0.53 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[TRIM47]] | -0.53 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ANKRD49]] | -0.52 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[SNW1]] | -0.52 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[JAGN1]] | -0.51 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[CARD6]] | -0.51 | -0.51 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P3H3]] | B | P3H3 activity raises FKBP10's level | lines that do not express P3H3 (10) vs lines expressing it (40) | 2.18× lower at baseline in the lines without P3H3 | 0.090 | ⚠ within organs, on part of the lines; also absent: STARD9, GSTA4, CTXN1 |
| [[POGLUT2]] | C | POGLUT2 activity raises FKBP10's level | lines that do not express POGLUT2 (4) vs lines expressing it (46) | 4.90× lower at baseline in the lines without POGLUT2 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYCP2L, BIVM, DUSP19; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POGLUT2]] | B | FKBP10 activity raises POGLUT2's level | lines that do not express FKBP10 (10) vs lines expressing it (40) | 1.81× lower at baseline in the lines without FKBP10 | 0.009 | ⚠ within organs, on part of the lines; also absent: MPP2, RAC3, BOLA3-DT |
| [[P3H4]] | B | FKBP10 activity raises P3H4's level | lines that do not express FKBP10 (10) vs lines expressing it (40) | 2.50× lower at baseline in the lines without FKBP10 | 0.014 | ⚠ within organs, on part of the lines; also absent: MPP2, RAC3, BOLA3-DT |
| [[LMAN1]] | B | FKBP10 activity raises LMAN1's level | lines that do not express FKBP10 (10) vs lines expressing it (40) | 1.56× lower at baseline in the lines without FKBP10 | 0.022 | ⚠ within organs, on part of the lines; also absent: MPP2, RAC3, BOLA3-DT |
| [[DLG4]] | B | FKBP10 activity raises DLG4's level | lines that do not express FKBP10 (10) vs lines expressing it (40) | 2.23× lower at baseline in the lines without FKBP10 | 0.031 | ⚠ within organs, on part of the lines; also absent: MPP2, RAC3, BOLA3-DT |
| [[P3H3]] | B | FKBP10 activity raises P3H3's level | lines that do not express FKBP10 (10) vs lines expressing it (40) | 2.20× lower at baseline in the lines without FKBP10 | 0.031 | ⚠ within organs, on part of the lines; also absent: MPP2, RAC3, BOLA3-DT |
| [[EML3]] | B | FKBP10 activity raises EML3's level | lines that do not express FKBP10 (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without FKBP10 | 0.040 | ⚠ within organs, on part of the lines; also absent: MPP2, RAC3, BOLA3-DT |
| [[PIK3R2]] | B | FKBP10 activity raises PIK3R2's level | lines that do not express FKBP10 (10) vs lines expressing it (40) | 1.26× lower at baseline in the lines without FKBP10 | 0.074 | ⚠ within organs, on part of the lines; also absent: MPP2, RAC3, BOLA3-DT |
| [[DDHD2]] | B | FKBP10 activity raises DDHD2's level | lines that do not express FKBP10 (10) vs lines expressing it (40) | 1.63× lower at baseline in the lines without FKBP10 | 0.091 | ⚠ within organs, on part of the lines; also absent: MPP2, RAC3, BOLA3-DT |

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.707). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.6, -29.5); signed map (-54.5, 5.2). **Vector** length 105, 28.3% of its response variance represented; |z| ≥ 3 in 881 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.50 to 11); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.50 to 9); *unfolded protein response* (hallmark, mean cos +0.52 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | -1.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.1 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +3.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.2 | -10.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.7 | -9.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -16.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.3 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.2 | -21.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -5.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | FKBP prolyl isomerase 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:41,812,680-41,823,213 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hFKBP65, FKBP65, FLJ22041, FKBP6, FLJ20683, FLJ23833 |
| Gene groups (HGNC) | EF-hand domain containing; FKBP prolyl isomerase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AY3](https://www.uniprot.org/uniprotkb/Q96AY3) (Peptidyl-prolyl cis-trans isomerase FKBP10):

> PPIases accelerate the folding of proteins during protein synthesis.

**Summary**, from NCBI Gene [60681](https://www.ncbi.nlm.nih.gov/gene/60681):

> The protein encoded by this gene belongs to the FKBP-type peptidyl-prolyl cis/trans isomerase (PPIase) family. This protein localizes to the endoplasmic reticulum and acts as a molecular chaperone. Alternatively spliced variants encoding different isoforms have been reported, but their biological validity has not been determined.[provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:18169](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18169) · Entrez [60681](https://www.ncbi.nlm.nih.gov/gene/60681) · UniProt [Q96AY3](https://www.uniprot.org/uniprotkb/Q96AY3) · Ensembl [ENSG00000141756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141756)

## Data

Gene col 6573: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6573); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6573, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6573]; `tensor/DDL_lfc|DDL_z.npy` [6573]; `embed/gene_vectors.npy` [6573]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6573 or target_col == 6573). Every well: [[FKBP10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FKBP10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
