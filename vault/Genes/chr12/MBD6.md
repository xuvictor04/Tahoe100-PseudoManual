---
symbol: "MBD6"
type: "gene"
col: 9401
ensembl_id: "ENSG00000166987"
name: "methyl-CpG binding domain protein 6"
location: "12q13.3"
module: 96
arm: "+"
pooled_cpm: 18.44
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# MBD6

*methyl-CpG binding domain protein 6* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.88× (z +10.9, q 6e-25, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.567× (z -10.0, q 7e-21, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DXO]] (+0.70, fdr 7e-06), [[CNOT3]] (+0.65, fdr 7e-06), [[GPR108]] (+0.65, fdr 1e-05); moves opposite to [[SNTB2]] (-0.51, fdr 3e-05), [[ANKRD16]] (-0.49, fdr 4e-05), [[TBC1D4]] (-0.48, fdr 4e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9401.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +10.9 | 6e-25 | 35/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.68×** | +6.8 | 3e-09 | 31/46 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.7 | 2e-06 | 2/48 (NCI-H1792, PANC-1) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +5.1 | 5e-05 | 22/42 (Hs 766T, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Artesunate (drug)]] 5 µM |  | **1.31×** | +4.6 | 5e-04 | 23/48 (HEC-1-A, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +4.5 | 7e-04 | 16/34 (SW 900, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.38×** | +4.3 | 0.001 | 21/47 (C-33 A, SW480, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.37×** | +4.3 | 0.001 | 20/47 (RKO, HEC-1-A, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +4.3 | 0.001 | 18/47 (A-172, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +4.1 | 0.002 | 15/32 (AsPC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 0.003 | 18/46 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.70×** | +3.8 | 0.007 | 11/46 (A-427, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.32×** | +3.8 | 0.007 | 21/40 (A498, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.7 | 0.008 | 17/43 (HS-578T, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.27×** | +3.2 | 0.057 | 11/48 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.24×** | +2.9 | 0.094 | 8/47 (C-33 A, BT-474, …) | rises with dose | position effect removed |
| [[crizotinib (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.094 | 5/47 (PANC-1, AsPC-1, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.26×** | +2.9 | 0.094 | 13/45 (hTERT-HPNE, SW1417, …) | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **1.24×** | +2.9 | 0.094 | 10/48 (C-33 A, BT-474, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9401.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.567×** | -10.0 | 7e-21 | 43/47 (NCI-H1792, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.562×** | -7.7 | 5e-12 | 34/46 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -5.2 | 4e-05 | 26/46 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~23% here); position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.693×** | -5.1 | 5e-05 | 21/47 (HepG2/C3A, RPMI-7951, …) | inconsistent across doses |  |
| [[Voriconazole (drug)]] 5 µM |  | **0.750×** | -4.0 | 0.006 | 17/47 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | **0.750×** | -4.0 | 0.006 | 18/47 (SW 1271, HS-578T, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.756×** | -3.9 | 0.008 | 16/47 (A-427, NCI-H460, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.823×** | -3.8 | 0.012 | 16/48 (A-427, RPMI-7951, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.773×** | -3.6 | 0.020 | 18/46 (NCI-H2030, H4, …) | inconsistent across doses | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | **0.788×** | -3.3 | 0.048 | 10/47 (CFPAC-1, A-172, …) | rises with dose | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.800×** | -3.1 | 0.090 | 11/47 (C-33 A, A-427, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.803×** | -3.1 | 0.099 | 15/47 (COLO 205, KATO III, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9401. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 36.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +11.8) | — |
| [[HT-29 (line)]] | alt | 35.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -11.5) |
| [[LoVo (line)]] | wt | 31.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -10.6) |
| [[PANC-1 (line)]] | alt | 18.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +16.8) | — |
| [[A-172 (line)]] | wt | 15.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +9.4) | — |
| [[COLO 205 (line)]] | alt | 19.3 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.185× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 11.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 55.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -13.7) |
| [[Panc 03.27 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -9.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9401), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DXO]] | +0.70 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[CNOT3]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[GPR108]] | +0.65 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[PRR14]] | +0.64 | +0.71 / +0.56 | both halves | 1e-05 | STRING 436 |
| [[TFE3]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[TNKS1BP1]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[SLC4A2]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[LRCH4]] | +0.60 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[GRIPAP1]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[PBX2]] | +0.59 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[HS1BP3]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[AAAS]] | +0.59 | +0.54 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNTB2]] | -0.51 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[ANKRD16]] | -0.49 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[TBC1D4]] | -0.48 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[PDK1-AS1]] | -0.48 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[SNRPB]] | -0.48 | -0.41 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MBD6's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-12.3, 4.6); signed map (11.7, -17.4). **Vector** length 91.9, 19.5% of its response variance represented; |z| ≥ 3 in 791 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +4.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +5.4 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +3.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.9 | +6.8 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +2.9 | +4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +2.8 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +2.6 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -10.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -5.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -7.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.3 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -2.0 | -5.1 |
|  | [[vincristine (drug)]] 0.05 µM |  | -2.0 | -1.7 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | methyl-CpG binding domain protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:57,520,710-57,530,148 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1887 |
| Gene groups (HGNC) | Methyl-CpG binding domain containing |
| Reactome | 2 pathways, smallest: UCH proteinases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DN6](https://www.uniprot.org/uniprotkb/Q96DN6) (Methyl-CpG-binding domain protein 6):

> Non-catalytic component of the polycomb repressive deubiquitinase (PR-DUB) complex, a complex that specifically mediates deubiquitination of histone H2A monoubiquitinated at 'Lys-120' (H2AK119ub1). Important for stability of PR-DUB components and stimulating its ubiquitinase activity. As part of the PR-DUB complex, associates with chromatin enriched in histone marks H3K4me1, H3K4me3, and H3K27Ac, but not in H3K27me3. MBD5 and MBD6 containing complexes associate with distinct chromatin regions …

**Summary**, from NCBI Gene [114785](https://www.ncbi.nlm.nih.gov/gene/114785):

> Enables chromatin binding activity. Located in chromocenter and nucleoplasm. Implicated in autism spectrum disorder. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20445](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20445) · Entrez [114785](https://www.ncbi.nlm.nih.gov/gene/114785) · UniProt [Q96DN6](https://www.uniprot.org/uniprotkb/Q96DN6) · Ensembl [ENSG00000166987](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166987)

## Data

Gene col 9401: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9401); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9401, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9401]; `tensor/DDL_lfc|DDL_z.npy` [9401]; `embed/gene_vectors.npy` [9401]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9401 or target_col == 9401). Every well: [[MBD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MBD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
