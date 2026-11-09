---
symbol: "KAT6B"
type: "gene"
col: 8003
ensembl_id: "ENSG00000156650"
name: "lysine acetyltransferase 6B"
location: "10q22.2"
module: 95
arm: "+"
pooled_cpm: 182.4
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 46
n_dd_up_clean: 3
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# KAT6B

*lysine acetyltransferase 6B* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[GSK1059615 (drug)]] 5 µM: 1.45× (z +4.9, q 4e-04, up in 31 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 46 drug-doses (19 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.242× (z -35.8, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HBP1]] (+0.62, fdr 7e-05), [[EP300]] (+0.61, fdr 4e-05), [[DRC3]] (+0.61, fdr 3e-05); moves opposite to [[MAPKAPK3]] (-0.55, fdr 3e-05), [[PRRG1]] (-0.55, fdr 8e-05), [[TMEM241]] (-0.55, fdr 6e-05).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8003.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **1.45×** | +4.9 | 4e-04 | 31/49 (A498, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.37×** | +4.2 | 0.007 | 28/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.014 | 20/50 (A-427, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 1.14× | +3.3 | 0.16 | 14/49 (RPMI-7951, NCI-H2347, …) | top dose only | plate-row cell shift |
| [[XRK3F2 (drug)]] 5 µM |  | 1.26× | +3.1 | 0.20 | 9/48 (SW480, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.09× | +3.0 | 0.25 | 0/48 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 23 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 46 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8003.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.242×** | -35.8 | 0e+00 | 48/48 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.277×** | -32.3 | 0e+00 | 48/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.307×** | -29.8 | 0e+00 | 48/48 (NCI-H1792, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.338×** | -27.4 | 0e+00 | 48/48 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.349×** | -26.5 | 0e+00 | 48/48 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.409×** | -22.5 | 0e+00 | 45/49 (SK-MEL-2, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.413×** | -21.4 | 0e+00 | 44/44 (LoVo, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.413×** | -21.2 | 0e+00 | 48/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.449×** | -18.6 | 0e+00 | 43/45 (A-427, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.498×** | -17.5 | 0e+00 | 46/48 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.318×** | -15.1 | 0e+00 | 48/49 (HOP62, SNU-423, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.660×** | -14.7 | 0e+00 | 43/48 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.385×** | -12.6 | 1e-34 | 48/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.405×** | -11.9 | 5e-31 | 47/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.420×** | -11.4 | 1e-28 | 46/48 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.442×** | -10.8 | 2e-25 | 45/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.654×** | -10.7 | 5e-25 | 44/49 (LOX-IMVI, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.656×** | -10.6 | 9e-25 | 33/48 (MIA PaCa-2, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.472×** | -9.9 | 1e-21 | 45/48 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8003. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 215 | 0 | 31 (14 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.202× (z -23.8) |
| [[PANC-1 (line)]] | alt | 238 | 0 | 21 (8 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.242× (z -21.5) |
| [[MIA PaCa-2 (line)]] | alt | 176 | 0 | 20 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.192× (z -25.8) ⚠ unreliable plate only · without an alert: [[Belinostat (drug)]] 5 µM 0.225× (z -24.5) |
| [[SNU-423 (line)]] | alt | 280 | 0 | 20 (10 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.141× (z -27.6) |
| [[C32 (line)]] | wt | 218 | 1 | 18 (9 ⚠) | [[PH-797804 (drug)]] 5 µM 3.41× (z +9.2) | [[Belinostat (drug)]] 5 µM 0.125× (z -29.7) |
| [[CFPAC-1 (line)]] | alt | 238 | 0 | 19 (10 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.167× (z -25.3) |
| [[HOP62 (line)]] | alt | 227 | 0 | 19 (10 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.120× (z -31.9) |
| [[HT-29 (line)]] | alt | 210 | 0 | 17 (7 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.241× (z -22.3) |
| [[HS-578T (line)]] | alt | 203 | 0 | 16 (7 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.132× (z -25.3) |
| [[NCI-H1792 (line)]] | alt | 247 | 0 | 16 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.115× (z -27.8) |
| [[SW 900 (line)]] | alt | 200 | 0 | 15 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.243× (z -19.3) |
| [[LOX-IMVI (line)]] | wt | 160 | 0 | 14 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.161× (z -26.2) |
| [[SW480 (line)]] | alt | 195 | 0 | 14 (8 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.351× (z -18.2) |
| [[H4 (line)]] | wt | 165 | 0 | 13 (7 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.159× (z -19.8) |
| [[hTERT-HPNE (line)]] | wt | 248 | 0 | 13 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.142× (z -22.1) |
| [[HCT15 (line)]] | alt | 262 | 0 | 12 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.168× (z -23.3) |
| [[LoVo (line)]] | wt | 135 | 0 | 12 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0854× (z -34.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.258× (z -19.4) |
| [[NCI-H2030 (line)]] | alt | 216 | 0 | 12 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.248× (z -18.1) |
| [[SK-MEL-2 (line)]] | alt | 120 | 0 | 12 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -25.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.261× (z -16.8) |
| [[Hs 766T (line)]] | wt | 163 | 0 | 11 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.226× (z -17.8) |
| [[NCI-H2347 (line)]] | alt | 171 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -19.9) |
| [[SNU-1 (line)]] | wt | 204 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0779× (z -29.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.259× (z -16.4) |
| [[A-172 (line)]] | wt | 149 | 0 | 10 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.178× (z -21.4) |
| [[NCI-H1573 (line)]] | alt | 223 | 0 | 10 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.146× (z -27.5) |
| [[A498 (line)]] | wt | 115 | 0 | 9 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.263× (z -20.3) |
| [[AsPC-1 (line)]] | alt | 150 | 0 | 9 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.253× (z -17.1) |
| [[LS 180 (line)]] | wt | 308 | 0 | 9 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.208× (z -23.2) |
| [[RPMI-7951 (line)]] | alt | 170 | 0 | 9 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.162× (z -21.3) |
| [[AN3 CA (line)]] | alt | 258 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.287× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 127 | 0 | 8 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -26.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.356× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 167 | 0 | 8 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.167× (z -23.6) |
| [[A-427 (line)]] | wt | 111 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0932× (z -27.6) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.454× (z -9.9) |
| [[KATO III (line)]] | alt | 129 | 0 | 7 (3 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.396× (z -10.7) |
| [[SW1417 (line)]] | alt | 150 | 0 | 7 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.290× (z -17.2) |
| [[SW48 (line)]] | wt | 181 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.219× (z -15.3) |
| [[CHP-212 (line)]] | wt | 246 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.192× (z -13.3) |
| [[HepG2_C3A (line)]] | wt | 154 | 0 | 6 | — | [[Belinostat (drug)]] 0.5 µM 0.248× (z -15.8) |
| [[C-33 A (line)]] | alt | 183 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.426× (z -10.1) |
| [[COLO 205 (line)]] | alt | 203 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.212× (z -18.3) |
| [[HEC-1-A (line)]] | alt | 189 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.284× (z -23.7) |
| [[J82 (line)]] | alt | 86.5 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.237× (z -18.7) |
| [[A549 (line)]] | wt | 143 | 0 | 4 | — | [[Belinostat (drug)]] 0.5 µM 0.282× (z -13.2) |
| [[BT-474 (line)]] | alt | 141 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.372× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.423× (z -9.6) |
| [[SW 1088 (line)]] | alt | 174 | 0 | 3 | — | [[Panobinostat (drug)]] 0.05 µM 0.0945× (z -11.3) |
| [[RKO (line)]] | wt | 110 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.391× (z -9.6) |
| [[SHP-77 (line)]] | alt | 74.1 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.424× (z -8.9) |
| [[NCI-H2122 (line)]] | alt | 201 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0534× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H596 (line)]] | alt | 195 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.323× (z -10.9) ⚠ transcription drop |
| [[NCI-H661 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 131 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8003), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HBP1]] | +0.62 | +0.37 / +0.70 | both halves | 7e-05 |  |
| [[EP300]] | +0.61 | +0.43 / +0.68 | both halves | 4e-05 | pathway: Chromatin modifying enzymes; STRING 729 |
| [[DRC3]] | +0.61 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[RBM48]] | +0.60 | +0.37 / +0.67 | both halves | 7e-05 |  |
| [[SLU7]] | +0.60 | +0.35 / +0.61 | both halves | 1e-04 |  |
| [[CREBBP]] | +0.59 | +0.43 / +0.65 | both halves | 3e-05 | pathway: Chromatin modifying enzymes; STRING 582 |
| [[ATOSA]] | +0.59 | +0.26 / +0.65 | both halves | 4e-04 |  |
| [[CRNKL1]] | +0.59 | +0.30 / +0.64 | both halves | 2e-04 |  |
| [[PRPF18]] | +0.56 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[RFX1]] | +0.56 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[GTF2IRD2B]] | +0.55 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[NUDT16L1]] | +0.55 | +0.40 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK3]] | -0.55 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[PRRG1]] | -0.55 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[TMEM241]] | -0.55 | -0.38 / -0.60 | both halves | 6e-05 |  |
| [[ANKS6]] | -0.55 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[POLR3G]] | -0.55 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[LIMK1]] | -0.54 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[PLAAT1]] | -0.52 | -0.38 / -0.63 | both halves | 6e-05 |  |
| [[CCND2]] | -0.51 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[GNPNAT1]] | -0.50 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[ADAT2]] | -0.49 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[MCOLN2]] | -0.47 | -0.22 / -0.54 | both halves | 6e-04 |  |
| [[PVR]] | -0.47 | -0.49 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers KAT6B's level | compounds that target MTOR: 3 of 8 raise it (Bimiralisib, GSK1059615, Sapanisertib) | 38% of the class's compounds vs 0.8% of all compounds | 0.020 | ⚠ off-target possible; 3 compounds |
| [[PIK3CB]] | B | PIK3CB activity lowers KAT6B's level | compounds that target PIK3CB: 2 of 3 raise it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 0.8% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |
| [[PIK3CA]] | B | PIK3CA activity lowers KAT6B's level | compounds that target PIK3CA: 2 of 4 raise it (Bimiralisib, GSK1059615) | 50% of the class's compounds vs 0.8% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.483). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-43.0, 19.4); signed map (-2.2, 6.8). **Vector** length 113, 43.7% of its response variance represented; |z| ≥ 3 in 1,934 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | +1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.3 | +2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +4.2 | -7.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.0 | -2.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.4 | +4.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.2 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -12.8 | -21.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -11.0 | -26.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -10.7 | -10.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -10.7 | -14.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -9.5 | -27.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.8 | -11.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.8 | -12.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.7 | -9.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.7 | -11.4 |

## What is on record

|  |  |
|---|---|
| Name | lysine acetyltransferase 6B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:74,824,927-75,032,624 (+) |
| Ensembl biotype | protein_coding |
| Also known as | querkopf, qkf, Morf, MOZ2; previously MYST4 |
| Gene groups (HGNC) | PHD finger proteins; MYST type domain containing lysine acetyltransferases; Zinc fingers MYST C2HC-type |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WYB5](https://www.uniprot.org/uniprotkb/Q8WYB5) (Histone acetyltransferase KAT6B):

> Histone acetyltransferase which may be involved in both positive and negative regulation of transcription. Required for RUNX2-dependent transcriptional activation. May be involved in cerebral cortex development. Component of the MOZ/MORF complex which has a histone H3 acetyltransferase activity.

**Summary**, from NCBI Gene [23522](https://www.ncbi.nlm.nih.gov/gene/23522):

> The protein encoded by this gene is a histone acetyltransferase and component of the MOZ/MORF protein complex. In addition to its acetyltransferase activity, the encoded protein has transcriptional activation activity in its N-terminal end and transcriptional repression activity in its C-terminal end. This protein is necessary for RUNX2-dependent transcriptional activation and could be involved in brain development. Mutations have been found in patients with genitopatellar syndrome. A …

**Accessions** — [HGNC:17582](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17582) · Entrez [23522](https://www.ncbi.nlm.nih.gov/gene/23522) · UniProt [Q8WYB5](https://www.uniprot.org/uniprotkb/Q8WYB5) · Ensembl [ENSG00000156650](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156650)

## Data

Gene col 8003: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8003); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8003, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8003]; `tensor/DDL_lfc|DDL_z.npy` [8003]; `embed/gene_vectors.npy` [8003]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8003 or target_col == 8003). Every well: [[KAT6B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KAT6B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
