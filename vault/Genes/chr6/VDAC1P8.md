---
symbol: "VDAC1P8"
type: "gene"
col: 13688
ensembl_id: "ENSG00000229036"
name: "voltage dependent anion channel 1 pseudogene 8"
location: "6q24.2"
module: 207
arm: "+"
pooled_cpm: 5.39
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/207"]
generated_by: "tahoemap"
---

# VDAC1P8

*voltage dependent anion channel 1 pseudogene 8* — 6q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.20× (z +9.5, q 2e-18, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Belumosudil (drug)]] 5 µM: 0.582× (z -6.2, q 2e-07, down in 19 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW480 0.184×, NCI-H460 0.170×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 1 line (HOP62 0.102×; ⚠ transcription drop; cell-cycle shift, would explain all of this change); [[Rapamycin (drug)]] 0.05 µM in 1 line (SW1417 0.0438×); [[Monocrotaline (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0754×); [[Relugolix (drug)]] 0.5 µM in 1 line (COLO 205 0.0552×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSNAX-DISC1]] (+0.67, fdr 7e-06), [[C9orf153]] (+0.63, fdr 7e-06), [[GNRH1]] (+0.62, fdr 2e-05); moves opposite to [[CENPB]] (-0.65, fdr 1e-05), [[TMEM185B]] (-0.60, fdr 1e-05), [[DDX10]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 207]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DNAH14]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13688.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.20×** | +9.5 | 2e-18 | 34/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +8.1 | 1e-13 | 25/37 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +7.9 | 6e-13 | 25/39 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +7.1 | 2e-10 | 24/41 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +6.8 | 1e-09 | 13/30 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +6.6 | 4e-09 | 24/47 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +6.0 | 1e-07 | 16/43 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +4.5 | 5e-04 | 19/46 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.39×** | +3.9 | 0.006 | 7/47 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.24×** | +3.6 | 0.017 | 11/48 (NCI-H23, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.34×** | +3.3 | 0.046 | 9/43 (PANC-1, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13688.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW480 0.184×, NCI-H460 0.170×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 1 line (HOP62 0.102×; ⚠ transcription drop; cell-cycle shift, would explain all of this change); [[Rapamycin (drug)]] 0.05 µM in 1 line (SW1417 0.0438×); [[Monocrotaline (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0754×); [[Relugolix (drug)]] 0.5 µM in 1 line (COLO 205 0.0552×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.582×** | -6.2 | 2e-07 | 19/44 (NCI-H1573, C32, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.620×** | -5.5 | 1e-05 | 17/33 (A549, A-172, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.735×** | -3.6 | 0.072 | 13/46 (HOP62, NCI-H2030, …) | rises with dose | composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.777× | -3.0 | 0.34 | 5/45 (HepG2/C3A, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13688. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 4.76 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0932× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.0901× (z -8.5) |
| [[SW480 (line)]] | alt | 6.98 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -9.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 4.90 | 0 | 1 | — | [[Relugolix (drug)]] 0.5 µM 0.0552× (z -8.7) |
| [[HOP62 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.102× (z -12.2) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 9.40 | 0 | 1 | — | [[Monocrotaline (drug)]] 5 µM 0.0754× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 5.88 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -8.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 2.79 | 0 | 1 | — | [[Rapamycin (drug)]] 0.05 µM 0.0438× (z -10.0) |
| [[A-172 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13688), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSNAX-DISC1]] | +0.67 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[C9orf153]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[GNRH1]] | +0.62 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[DNAJC25]] | +0.62 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[HELZ]] | +0.62 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[APTR]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[BCKDHA]] | +0.62 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[COG7]] | +0.61 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[SRP54-AS1]] | +0.61 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[CRYBB2P1-1]] | +0.61 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[EMC1-AS1]] | +0.61 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[PMS2P4-1]] | +0.61 | +0.67 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPB]] | -0.65 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[TMEM185B]] | -0.60 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[DDX10]] | -0.60 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[RABGAP1L]] | -0.59 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[HERPUD2-AS1]] | -0.59 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[RASAL2]] | -0.58 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[MGA]] | -0.56 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[B3GALT9]] | -0.56 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[UBE2E3]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[PITPNB]] | -0.54 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[TJP1]] | -0.53 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[DNAH14]] | -0.53 | -0.36 / -0.46 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAH14]] | B | DNAH14 activity raises VDAC1P8's level | lines that do not express DNAH14 (10) vs lines expressing it (40) | 1.21× lower at baseline in the lines without DNAH14 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF345, ZNF790, ENSG00000289516; its own permutation p |
| [[TOP2A]] | B | TOP2A activity lowers VDAC1P8's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 207]]; 15 genes; this gene is in the **+** arm (projection on the module's main direction 0.762). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (12.0, -23.2); signed map (-29.6, 26.9). **Vector** length 53.9, 6.83% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.5 | +7.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | +1.2 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +2.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +0.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.1 | +2.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.0 | +1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.9 | +2.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.9 | -5.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -6.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -0.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -2.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.8 | -2.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | voltage dependent anion channel 1 pseudogene 8 |
| Locus type | pseudogene |
| Location | 6q24.2 — chr6:143,490,515-143,491,367 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:37483](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37483) · Entrez [100310840](https://www.ncbi.nlm.nih.gov/gene/100310840) · Ensembl [ENSG00000229036](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229036)

## Data

Gene col 13688: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13688); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13688, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13688]; `tensor/DDL_lfc|DDL_z.npy` [13688]; `embed/gene_vectors.npy` [13688]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13688 or target_col == 13688). Every well: [[VDAC1P8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VDAC1P8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
