---
symbol: "LSM4"
type: "gene"
col: 5076
ensembl_id: "ENSG00000130520"
name: "LSM4 homolog, U6 small nuclear RNA and mRNA degradation associated"
location: "19p13.11"
module: 6
arm: "+"
pooled_cpm: 27.58
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# LSM4

*LSM4 homolog, U6 small nuclear RNA and mRNA degradation associated* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.31× (z +11.6, q 3e-28, up in 42 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H460 7.23×, NCI-H1573 12.8×, MIA PaCa-2 7.64×, A498 5.04×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Dinaciclib (drug)]] 5 µM in 7 lines (KATO III 8.92×, MIA PaCa-2 9.04×, A549 9.25×, NCI-H460 5.80×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.585× (z -5.7, q 9e-06, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BARD1]] (+0.73, fdr 7e-06), [[NCAPD3]] (+0.72, fdr 7e-06), [[TUBG1]] (+0.70, fdr 7e-06); moves opposite to [[NKAPD1]] (-0.65, fdr 9e-05), [[CDK3]] (-0.63, fdr 3e-05), [[RRAGB]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 13 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5076.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H460 7.23×, NCI-H1573 12.8×, MIA PaCa-2 7.64×, A498 5.04×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Dinaciclib (drug)]] 5 µM in 7 lines (KATO III 8.92×, MIA PaCa-2 9.04×, A549 9.25×, NCI-H460 5.80×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **5.31×** | +11.6 | 3e-28 | 42/43 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **4.31×** | +10.5 | 3e-23 | 38/38 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **3.33×** | +8.3 | 2e-14 | 40/41 (LoVo, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **1.97×** | +5.1 | 6e-05 | 40/45 (SW1417, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +4.8 | 2e-04 | 36/44 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.82×** | +4.5 | 8e-04 | 36/48 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.76×** | +4.2 | 0.002 | 32/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.65×** | +3.7 | 0.014 | 29/47 (NCI-H460, KATO III, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.40×** | +3.5 | 0.026 | 25/47 (NCI-H2347, A549, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.53×** | +3.2 | 0.086 | 22/47 (COLO 205, A549, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.35×** | +3.1 | 0.086 | 27/48 (PANC-1, SHP-77, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 1.53× | +3.1 | 0.10 | 24/48 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~92% of this change | 1.52× | +3.0 | 0.11 | 27/47 (SNU-423, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5076.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.585×** | -5.7 | 9e-06 | 37/47 (MIA PaCa-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.632×** | -3.4 | 0.069 | 24/47 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.422×** | -3.4 | 0.069 | 29/47 (LS 180, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.422×** | -3.4 | 0.069 | 30/47 (A-427, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.423×** | -3.4 | 0.069 | 30/48 (H4, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.425×** | -3.3 | 0.069 | 32/48 (A-427, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.623×** | -3.3 | 0.069 | 31/48 (SHP-77, A498, …) | inconsistent across doses |  |
| [[Tadalafil (drug)]] 5 µM |  | **0.638×** | -3.2 | 0.090 | 27/47 (A-172, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, +0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5076. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 26.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 9.04× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -12.6) |
| [[A498 (line)]] | wt | 39.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[A549 (line)]] | wt | 17.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.25× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[HOP62 (line)]] | alt | 15.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.56× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[HT-29 (line)]] | alt | 28.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.17× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[LoVo (line)]] | wt | 24.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.96× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H460 (line)]] | wt | 19.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.23× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[SNU-1 (line)]] | wt | 21.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -10.7) |
| [[SNU-423 (line)]] | alt | 18.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.59× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[SW480 (line)]] | alt | 26.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.85× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[A-172 (line)]] | wt | 30.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[A-427 (line)]] | wt | 55.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 24.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.34× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[CFPAC-1 (line)]] | alt | 19.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.49× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[HEC-1-A (line)]] | alt | 48.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[HS-578T (line)]] | alt | 29.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.33× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[J82 (line)]] | alt | 36.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.71× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[KATO III (line)]] | alt | 25.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.92× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[LOX-IMVI (line)]] | wt | 16.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.96× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[LS 180 (line)]] | wt | 40.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.49× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H1573 (line)]] | alt | 13.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.8× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.34× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H23 (line)]] | alt | 31.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 42.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[PANC-1 (line)]] | alt | 34.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.07× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[RPMI-7951 (line)]] | alt | 19.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -8.7) |
| [[SW 900 (line)]] | alt | 16.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.19× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[SW1417 (line)]] | alt | 37.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[AN3 CA (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5076), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BARD1]] | +0.73 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[NCAPD3]] | +0.72 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[TUBG1]] | +0.70 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[TCF19]] | +0.69 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[MELK]] | +0.69 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[RFC4]] | +0.69 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[MYCBP]] | +0.68 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[TICRR]] | +0.68 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TK1]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[POC1A]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[UBE2T]] | +0.67 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[NHP2]] | +0.67 | +0.70 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 505 |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKAPD1]] | -0.65 | -0.66 / -0.36 | both halves | 9e-05 |  |
| [[CDK3]] | -0.63 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[RRAGB]] | -0.63 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[DNAJC2]] | -0.62 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[GPRASP3]] | -0.62 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[HPS1]] | -0.62 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[ZRANB2]] | -0.61 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[AIMP1]] | -0.61 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[EIF4EBP3]] | -0.60 | -0.56 / -0.30 | both halves | 2e-04 |  |
| [[AP5Z1]] | -0.60 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[METAP2]] | -0.59 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[WASHC1]] | -0.59 | -0.64 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity raises LSM4's level | compounds that target MTOR: 3 of 8 lower it (Bimiralisib, GSK1059615, Sapanisertib) | 38% of the class's compounds vs 1.7% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[ZNF367]] | C | ZNF367 activity raises LSM4's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 1.83× lower at baseline in the lines without ZNF367 | 0.042 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.650). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.4, -41.0); signed map (-36.8, -41.2). **Vector** length 61.9, 17.1% of its response variance represented; |z| ≥ 3 in 684 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Chromosome Maintenance* (reactome, mean cos +0.51 to 29); *Telomere C-strand (Lagging Strand) Synthesis* (reactome, mean cos +0.52 to 19); *Lagging Strand Synthesis* (reactome, mean cos +0.50 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.9 | +3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +2.9 | +4.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | +2.8 | +4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.0 | +2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +0.9 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +1.2 | -1.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.1 | +2.0 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | +1.1 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | -5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | -2.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.8 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | +1.6 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | +0.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.6 | -1.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | LSM4 homolog, U6 small nuclear RNA and mRNA degradation associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,306,236-18,323,112 (-) |
| Ensembl biotype | protein_coding |
| Also known as | YER112W |
| Gene groups (HGNC) | LSm proteins |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 6 pathways, smallest: mRNA decay by 5' to 3' exoribonuclease; Deadenylation-dependent mRNA decay; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4Z0](https://www.uniprot.org/uniprotkb/Q9Y4Z0) (U6 snRNA-associated Sm-like protein LSm4):

> Plays a role in pre-mRNA splicing as component of the U4/U6-U5 tri-snRNP complex that is involved in spliceosome assembly, and as component of the precatalytic spliceosome (spliceosome B complex). The heptameric LSM2-8 complex binds specifically to the 3'-terminal U-tract of U6 snRNA.

**Summary**, from NCBI Gene [25804](https://www.ncbi.nlm.nih.gov/gene/25804):

> This gene encodes a member of the LSm family of RNA-binding proteins. LSm proteins form stable heteromers that bind specifically to the 3'-terminal oligo(U) tract of U6 snRNA and may play a role in pre-mRNA splicing by mediating U4/U6 snRNP formation. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:17259](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17259) · Entrez [25804](https://www.ncbi.nlm.nih.gov/gene/25804) · UniProt [Q9Y4Z0](https://www.uniprot.org/uniprotkb/Q9Y4Z0) · Ensembl [ENSG00000130520](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130520)

## Data

Gene col 5076: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5076); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5076, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5076]; `tensor/DDL_lfc|DDL_z.npy` [5076]; `embed/gene_vectors.npy` [5076]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5076 or target_col == 5076). Every well: [[LSM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LSM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
