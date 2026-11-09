---
symbol: "GRPEL2"
type: "gene"
col: 8917
ensembl_id: "ENSG00000164284"
name: "GrpE like 2, mitochondrial"
location: "5q32"
module: 63
arm: "+"
pooled_cpm: 28.7
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# GRPEL2

*GrpE like 2, mitochondrial* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.80× (z +9.1, q 7e-17, up in 30 of 45 measured lines) ⚠ toxic. The strongest without an alert is [[Neratinib (maleate) (drug)]] 0.5 µM: 1.44× (z +5.8, q 7e-07, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.728× (z -4.9, q 5e-04, down in 18 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Arbutin (drug)]] 0.05 µM: 0.771× (z -3.5, q 0.065, down in 16 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 0.0804×, A-427 0.264×, PANC-1 0.415×, Panc 03.27 0.241×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 0.174×, PANC-1 0.444×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.324×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pravastatin (sodium) (drug)]] 0.05 µM in 1 line (COLO 205 0.0521×); [[Ciclopirox (drug)]] 0.05 µM in 1 line (CHP-212 0.0864×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIB3]] (+0.69, fdr 7e-06), [[CHAC1]] (+0.68, fdr 7e-06), [[SARS1]] (+0.66, fdr 1e-05); moves opposite to [[CCDC200]] (-0.50, fdr 1e-04), [[HIVEP2-DT]] (-0.49, fdr 4e-05), [[IL13RA1]] (-0.48, fdr 2e-04).
> It is in [[Module 063]], a single-armed module (ISR ATF4).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8917.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +9.1 | 7e-17 | 30/45 (NCI-H1573, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +7.5 | 2e-11 | 34/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +7.2 | 1e-10 | 35/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.44×** | +5.8 | 7e-07 | 29/48 (HEC-1-A, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +5.5 | 4e-06 | 21/48 (Panc 03.27, LOX-IMVI, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +5.4 | 6e-06 | 21/47 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.0 | 6e-05 | 22/48 (LOX-IMVI, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.34×** | +4.7 | 2e-04 | 22/45 (J82, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.30×** | +4.3 | 0.001 | 21/48 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.63×** | +4.1 | 0.002 | 21/48 (NCI-H460, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.003 | 20/48 (LoVo, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.8 | 0.007 | 16/48 (LOX-IMVI, A549, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.57×** | +3.8 | 0.007 | 13/47 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.56×** | +3.7 | 0.008 | 15/48 (LoVo, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +3.7 | 0.009 | 16/48 (NCI-H460, CFPAC-1, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.009 | 17/47 (C-33 A, NCI-H460, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.014 | 15/47 (NCI-H460, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.016 | 14/48 (HepG2/C3A, SW48, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.018 | 8/49 (A498, MIA PaCa-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.47×** | +3.3 | 0.029 | 14/47 (A498, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8917.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 0.0804×, A-427 0.264×, PANC-1 0.415×, Panc 03.27 0.241×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 0.174×, PANC-1 0.444×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.324×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pravastatin (sodium) (drug)]] 0.05 µM in 1 line (COLO 205 0.0521×); [[Ciclopirox (drug)]] 0.05 µM in 1 line (CHP-212 0.0864×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.728×** | -4.9 | 5e-04 | 18/38 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.793×** | -3.7 | 0.054 | 21/45 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Arbutin (drug)]] 0.05 µM |  | **0.771×** | -3.5 | 0.065 | 16/47 (SW1417, SW48, …) | inconsistent across doses | position effect removed |
| [[Arbutin (drug)]] 0.5 µM |  | **0.804×** | -3.5 | 0.065 | 13/47 (SW1417, A549, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8917. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 39.8 | 1 (1 ⚠) | 3 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.99× (z +9.4) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.0804× (z -21.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 38.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 35.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.415× (z -10.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 32.3 | 0 | 1 | — | [[Ciclopirox (drug)]] 0.05 µM 0.0864× (z -9.1) |
| [[COLO 205 (line)]] | alt | 14.3 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0521× (z -12.0) |
| [[LS 180 (line)]] | wt | 36.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 22.5 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.81× (z +10.8) ⚠ toxic | — |
| [[Panc 03.27 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -9.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 35.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.87× (z +8.5) | — |
| [[A-172 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 34.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8917), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIB3]] | +0.69 | +0.65 / +0.59 | both halves | 7e-06 | STRING 465 |
| [[CHAC1]] | +0.68 | +0.64 / +0.63 | both halves | 7e-06 | STRING 574 |
| [[SARS1]] | +0.66 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[HEATR6]] | +0.63 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[EIF2S2]] | +0.62 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[C1orf174]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[GARS1]] | +0.62 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[ASNS]] | +0.61 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[LINC00662]] | +0.61 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[MFSD9]] | +0.60 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[PET117]] | +0.60 | +0.39 / +0.60 | both halves | 5e-05 |  |
| [[SESN2]] | +0.60 | +0.56 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC200]] | -0.50 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[HIVEP2-DT]] | -0.49 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[IL13RA1]] | -0.48 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[ITGAV]] | -0.47 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[NID1]] | -0.47 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[YES1]] | -0.47 | -0.22 / -0.54 | both halves | 6e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.4, 49.7); signed map (-12.7, 25.7). **Vector** length 93.0, 20.4% of its response variance represented; |z| ≥ 3 in 784 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.53 to 16); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.56 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.56 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.8 | +7.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.8 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +3.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.0 | +3.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.8 | +5.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.5 | +4.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.1 | +3.7 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +3.0 | -0.1 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.8 | -3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.7 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -6.4 | +0.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.0 | -0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -0.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.8 | -1.1 |
|  | [[Arbutin (drug)]] 0.05 µM |  | -1.7 | -3.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.7 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | GrpE like 2, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:149,345,430-149,354,583 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp451C205, Mt-GrpE#2, FLJ23713 |
| Reactome | 2 pathways, smallest: Mitochondrial protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAA5](https://www.uniprot.org/uniprotkb/Q8TAA5) (GrpE protein homolog 2, mitochondrial):

> [Isoform 1]: Nucleotide exchange factor (NEF) for mitochondrial HSP70 (mt-HSP70/HSPA9), facilitating the release of ADP from HSPA9 to allow ATP rebinding, which is essential for the chaperone cycle. Functions as a component of the presequence translocase-associated motor (PAM) complex, which drives ATP-dependent import of proteins into the mitochondrial matrix. In the PAM complex, supports the HSPA9-driven pulling mechanism that translocates polypeptides through the TIM23 complex. Functions as …

**Summary**, from NCBI Gene [134266](https://www.ncbi.nlm.nih.gov/gene/134266):

> Predicted to enable adenyl-nucleotide exchange factor activity and unfolded protein binding activity. Predicted to be involved in protein import into mitochondrial matrix. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21060](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21060) · Entrez [134266](https://www.ncbi.nlm.nih.gov/gene/134266) · UniProt [Q8TAA5](https://www.uniprot.org/uniprotkb/Q8TAA5) · Ensembl [ENSG00000164284](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164284)

## Data

Gene col 8917: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8917); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8917, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8917]; `tensor/DDL_lfc|DDL_z.npy` [8917]; `embed/gene_vectors.npy` [8917]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8917 or target_col == 8917). Every well: [[GRPEL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRPEL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
