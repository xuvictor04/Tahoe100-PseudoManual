---
symbol: "METTL1"
type: "gene"
col: 446
ensembl_id: "ENSG00000037897"
name: "methyltransferase 1, tRNA methylguanosine"
location: "12q14.1"
module: 1
arm: "+"
pooled_cpm: 5.03
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 14
n_dd_up_clean: 8
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# METTL1

*methyltransferase 1, tRNA methylguanosine* — 12q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.15× (z +9.8, q 5e-20, up in 22 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.509× (z -8.7, q 2e-15, down in 26 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOL6]] (+0.78, fdr 7e-06), [[PNO1]] (+0.73, fdr 7e-06), [[DPH2]] (+0.72, fdr 7e-06); moves opposite to [[GTF2IP4]] (-0.64, fdr 1e-05), [[GINM1]] (-0.63, fdr 2e-05), [[USP33]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HSF2BP]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 446.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.15×** | +9.8 | 5e-20 | 22/39 (NCI-H1792, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.86×** | +8.0 | 5e-13 | 8/22 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.77×** | +7.3 | 4e-11 | 22/45 (SW480, KATO III, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +6.7 | 2e-09 | 6/13 (A498, J82, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **2.11×** | +5.0 | 6e-05 | 6/32 (NCI-H1792, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.48×** | +4.8 | 2e-04 | 11/43 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +4.6 | 3e-04 | 19/44 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.97×** | +4.6 | 3e-04 | 1/36 (LoVo) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.29×** | +4.6 | 3e-04 | 17/40 (A498, NCI-H1573, …) | two highest doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.1 | 0.002 | 11/34 (NCI-H460, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.008 | 12/45 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +3.7 | 0.010 | 2/8 (A498, J82) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.73×** | +3.7 | 0.010 | 4/42 (NCI-H1792, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Isocorydine (drug)]] 5 µM |  | 1.19× | +3.1 | 0.066 | 2/46 (Panc 03.27, NCI-H1792) | rises with dose | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.59×** | +3.1 | 0.067 | 3/30 (AsPC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.080 | 7/46 (NCI-H1792, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 446.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.509×** | -8.7 | 2e-15 | 26/45 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.552×** | -7.7 | 5e-12 | 23/47 (SW48, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.606×** | -6.4 | 2e-08 | 19/46 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.635×** | -5.9 | 7e-07 | 19/44 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.649×** | -5.6 | 3e-06 | 16/46 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.483×** | -4.9 | 9e-05 | 13/42 (A-427, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.521×** | -4.4 | 9e-04 | 11/43 (NCI-H23, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.787×** | -4.4 | 9e-04 | 11/45 (HEC-1-A, RPMI-7951, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.563×** | -3.9 | 0.007 | 7/34 (NCI-H1792, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.743×** | -3.8 | 0.007 | 13/40 (Hs 766T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 0.5 µM |  | **0.764×** | -3.5 | 0.026 | 6/41 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.831×** | -3.4 | 0.034 | 7/45 (Hs 766T, AsPC-1, …) | top dose only |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.786×** | -3.1 | 0.085 | 2/46 (NCI-H661, LOX-IMVI) | inconsistent across doses |  |
| [[Verapamil (drug)]] 5 µM |  | **0.779×** | -3.0 | 0.093 | 6/44 (SW480, Panc 03.27, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 446. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 6.83 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -9.8) ⚠ cell-cycle shift, explains ~2% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.174× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 4.67 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.105× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 4.39 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0600× (z -10.1) ⚠ toxic |
| [[A-172 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 446), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOL6]] | +0.78 | +0.82 / +0.73 | both halves | 7e-06 |  |
| [[PNO1]] | +0.73 | +0.75 / +0.67 | both halves | 7e-06 | STRING 628 |
| [[DPH2]] | +0.72 | +0.76 / +0.67 | both halves | 7e-06 | STRING 547 |
| [[PUS1]] | +0.72 | +0.75 / +0.67 | both halves | 7e-06 | pathway: tRNA modification in the nucleus and cytosol; STRING 805 |
| [[TRMT61A]] | +0.71 | +0.79 / +0.66 | both halves | 7e-06 | same gene group; pathway: tRNA modification in the nucleus and cytosol; STRING 964 |
| [[CYP27B1]] | +0.71 | +0.68 / +0.60 | both halves | 7e-06 | STRING 782; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[GRWD1]] | +0.70 | +0.66 / +0.72 | both halves | 7e-06 | STRING 754 |
| [[PPRC1]] | +0.70 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[EMG1]] | +0.70 | +0.67 / +0.68 | both halves | 7e-06 | same gene group |
| [[IMP4]] | +0.69 | +0.76 / +0.63 | both halves | 7e-06 | STRING 632 |
| [[ZPR1]] | +0.69 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[GPATCH4]] | +0.68 | +0.66 / +0.62 | both halves | 7e-06 | STRING 439 |
| [[DHX37]] | +0.68 | +0.63 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2IP4]] | -0.64 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[GINM1]] | -0.63 | -0.64 / -0.46 | both halves | 2e-05 |  |
| [[USP33]] | -0.61 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[COX6A1]] | -0.61 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[SLC9A6]] | -0.61 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[GNB2]] | -0.61 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[NENF]] | -0.60 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[ARL3]] | -0.59 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[ARL6IP5]] | -0.59 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[PPP2R5A]] | -0.59 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[RECK]] | -0.59 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.58 | -0.58 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSF2BP]] | C | HSF2BP activity raises METTL1's level | lines that do not express HSF2BP (4) vs lines expressing it (46) | 1.41× lower at baseline in the lines without HSF2BP | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.679). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.2, -34.9); signed map (-2.3, -44.9). **Vector** length 61.6, 8.77% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.53 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.55 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.55 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +9.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +3.1 | +4.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.8 | +4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.6 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.0 | +4.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.1 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -2.4 | -6.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -4.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.2 | -8.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.0 | -4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase 1, tRNA methylguanosine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.1 — chr12:57,768,471-57,772,119 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRM8, TRMT8; previously C12orf1 |
| Gene groups (HGNC) | 7BS N7-guanosine RNA methyltransferases; DNA/RNA methyltransferases |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBP6](https://www.uniprot.org/uniprotkb/Q9UBP6) (tRNA):

> Catalytic component of METTL1-WDR4 methyltransferase complex that mediates the formation of N(7)-methylguanine in a subset of RNA species, such as tRNAs, mRNAs and microRNAs (miRNAs). Catalyzes the formation of N(7)-methylguanine at position 46 (m7G46) in a large subset of tRNAs that contain the 5'-RAGGU-3' motif within the variable loop. M7G46 interacts with C13-G22 in the D-loop to stabilize tRNA tertiary structure and protect tRNAs from decay. Also acts as a methyltransferase for a subset of …

**Summary**, from NCBI Gene [4234](https://www.ncbi.nlm.nih.gov/gene/4234):

> This gene is similar in sequence to the S. cerevisiae YDL201w gene. The gene product contains a conserved S-adenosylmethionine-binding motif and is inactivated by phosphorylation. Alternative splice variants encoding different protein isoforms have been described for this gene. A pseudogene has been identified on chromosome X. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7030](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7030) · Entrez [4234](https://www.ncbi.nlm.nih.gov/gene/4234) · UniProt [Q9UBP6](https://www.uniprot.org/uniprotkb/Q9UBP6) · Ensembl [ENSG00000037897](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000037897)

## Data

Gene col 446: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 446); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 446, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 446]; `tensor/DDL_lfc|DDL_z.npy` [446]; `embed/gene_vectors.npy` [446]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 446 or target_col == 446). Every well: [[METTL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
