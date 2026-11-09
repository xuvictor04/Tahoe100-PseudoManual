---
symbol: "LENG8-AS1"
type: "gene"
col: 13550
ensembl_id: "ENSG00000226696"
name: "LENG8 antisense RNA 1"
location: "19q13.42"
module: 15
arm: "+"
pooled_cpm: 7.11
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 17
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# LENG8-AS1

*LENG8 antisense RNA 1* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.10× (z +9.9, q 4e-20, up in 36 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.445× (z -7.4, q 1e-10, down in 31 of 46 measured lines) ⚠ cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.640× (z -4.2, q 0.003, down in 17 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF3C2-AS2]] (+0.74, fdr 7e-06), [[RABL2A]] (+0.67, fdr 1e-05), [[ERVK13-1]] (+0.67, fdr 3e-05); moves opposite to [[HPF1]] (-0.67, fdr 3e-05), [[ATP5PO]] (-0.63, fdr 5e-05, ⚠ ATP5PO in the vector space only through flagged drug-doses), [[TTBK2]] (-0.61, fdr 3e-05), [[ALAD]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DNAAF10]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13550.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +9.9 | 4e-20 | 36/41 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.27×** | +7.7 | 3e-12 | 31/48 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.008 | 14/47 (A-172, HS-578T, …) | rises with dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.083 | 13/41 (Panc 03.27, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 1.38× | +3.0 | 0.23 | 1/44 (NCI-H460) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.40× | +3.0 | 0.23 | 16/38 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 12 with an alert ⚠; shown: the 15 strongest. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13550.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.445×** | -7.4 | 1e-10 | 31/46 (A498, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.577×** | -5.2 | 6e-05 | 24/46 (H4, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.629×** | -4.4 | 0.002 | 19/46 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **0.617×** | -4.4 | 0.002 | 19/37 (HS-578T, NCI-H1792, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.640×** | -4.2 | 0.003 | 17/46 (SNU-423, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.436×** | -4.1 | 0.004 | 18/43 (A498, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.656×** | -4.0 | 0.005 | 18/47 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.753×** | -3.8 | 0.010 | 21/42 (A498, HEC-1-A, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.677×** | -3.7 | 0.013 | 15/46 (NCI-H23, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | **0.678×** | -3.7 | 0.013 | 19/41 (A-172, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.695×** | -3.5 | 0.028 | 17/47 (PANC-1, J82, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.696×** | -3.4 | 0.028 | 17/41 (A-172, A498, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.610×** | -3.3 | 0.037 | 14/43 (NCI-H2347, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.514×** | -3.3 | 0.040 | 16/34 (HT-29, NCI-H460, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.708×** | -3.3 | 0.040 | 12/45 (RPMI-7951, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.65 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13550. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 12.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -12.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 7.08 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0689× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 8.91 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.106× (z -10.5) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -8.5) ⚠ cell-cycle shift, explains ~59% of this change |
| [[A549 (line)]] | wt | 8.30 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0984× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 6.31 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0686× (z -9.6) |
| [[COLO 205 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.107× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0713× (z -10.2) ⚠ transcription drop |
| [[HOP62 (line)]] | alt | 4.47 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.111× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 5.07 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0763× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 6.03 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0682× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~48% of this change |
| [[NCI-H460 (line)]] | wt | 3.66 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0809× (z -9.5) |
| [[A-427 (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13550), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF3C2-AS2]] | +0.74 | +0.64 / +0.64 | both halves | 7e-06 | same gene group |
| [[RABL2A]] | +0.67 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[ERVK13-1]] | +0.67 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[ACAD9]] | +0.67 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[ZNF213-AS1]] | +0.67 | +0.42 / +0.59 | both halves | 4e-05 | same gene group |
| [[DPY19L3-DT]] | +0.63 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[LY6G5B]] | +0.63 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[TRNT1]] | +0.62 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ANXA2R-OT1]] | +0.62 | +0.38 / +0.56 | both halves | 7e-05 |  |
| [[SIAH2-AS1]] | +0.61 | +0.37 / +0.48 | both halves | 7e-05 | same gene group |
| [[RABL2B]] | +0.61 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[WDR45]] | +0.61 | +0.39 / +0.53 | both halves | 5e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPF1]] | -0.67 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[ATP5PO]] ⚠ | -0.63 | -0.39 / -0.54 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TTBK2]] | -0.61 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[ALAD]] | -0.59 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[PAFAH1B3]] | -0.59 | -0.24 / -0.59 | both halves | 5e-04 |  |
| [[SNAPIN]] | -0.57 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[KBTBD6]] | -0.57 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[ISCA2]] | -0.56 | -0.37 / -0.46 | both halves | 9e-05 |  |
| [[COMMD8]] | -0.56 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[NDUFA8]] | -0.55 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[NTHL1]] | -0.55 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[PTPN13]] | -0.53 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[USP2]] | -0.53 | -0.25 / -0.48 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNAAF10]] | C | DNAAF10's natural level strengthens LENG8-AS1's drug response | DNAAF10's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.00; direction clear | 0.073 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.648). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-6.1, 20.2); signed map (28.8, -17.3). **Vector** length 65.8, 10.4% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.7 | +2.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.5 | +2.5 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +1.1 | +1.9 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +1.0 | +1.4 |
|  | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | +1.0 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -3.6 | -7.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -2.7 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -4.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.6 | -3.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.2 | -3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | LENG8 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.42 — chr19:54,444,807-54,449,430 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40705](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40705) · Entrez [104355426](https://www.ncbi.nlm.nih.gov/gene/104355426) · Ensembl [ENSG00000226696](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226696)

## Data

Gene col 13550: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13550); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13550, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13550]; `tensor/DDL_lfc|DDL_z.npy` [13550]; `embed/gene_vectors.npy` [13550]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13550 or target_col == 13550). Every well: [[LENG8-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LENG8-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
