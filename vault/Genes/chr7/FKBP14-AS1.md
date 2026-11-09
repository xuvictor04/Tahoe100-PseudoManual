---
symbol: "FKBP14-AS1"
type: "gene"
col: 13566
ensembl_id: "ENSG00000227014"
name: "FKBP14 antisense RNA 1"
location: "7p14.3"
module: 15
arm: "+"
pooled_cpm: 7.73
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# FKBP14-AS1

*FKBP14 antisense RNA 1* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.80× (z +18.7, q 0e+00, up in 39 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.449× (z -10.3, q 5e-22, down in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.492× (z -9.1, q 3e-17, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPESP1]] (+0.82, fdr 7e-06), [[SEC24B-AS1]] (+0.75, fdr 7e-06), [[ZNF213-AS1]] (+0.72, fdr 7e-06).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13566.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.80×** | +18.7 | 0e+00 | 39/41 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +7.3 | 6e-11 | 24/37 (SW480, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.8 | 1e-06 | 18/47 (SW1417, AN3 CA, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +5.4 | 1e-05 | 7/17 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +5.2 | 2e-05 | 15/47 (A-427, PANC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.7 | 2e-04 | 18/42 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +3.5 | 0.039 | 6/35 (A498, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.28× | +3.1 | 0.13 | 8/42 (A-427, NCI-H2030, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.27× | +3.1 | 0.13 | 14/29 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13566.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.449×** | -10.3 | 5e-22 | 33/48 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.492×** | -9.1 | 3e-17 | 25/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.587×** | -6.8 | 2e-09 | 27/47 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.621×** | -5.9 | 7e-07 | 19/46 (PANC-1, NCI-H1792, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.707×** | -4.4 | 1e-03 | 17/47 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.714×** | -4.3 | 0.002 | 13/45 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.719×** | -4.2 | 0.002 | 12/48 (PANC-1, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **0.729×** | -3.9 | 0.007 | 15/35 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.742×** | -3.8 | 0.009 | 12/48 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.815×** | -3.7 | 0.012 | 16/43 (PANC-1, HEC-1-A, …) | top dose only | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.759×** | -3.5 | 0.022 | 14/47 (NCI-H23, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.598×** | -3.4 | 0.027 | 10/45 (PANC-1, H4, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.766×** | -3.4 | 0.028 | 12/47 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | **0.776×** | -3.2 | 0.049 | 3/48 (SNU-423, PANC-1, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.629×** | -3.1 | 0.073 | 12/41 (SNU-423, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13566. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 17.1 | 0 | 9 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.152× (z -13.4) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.179× (z -12.2) |
| [[BT-474 (line)]] | alt | 9.46 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +8.7) | [[Auranofin (drug)]] 5 µM 0.0815× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 8.93 | 0 | 2 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0692× (z -9.7) |
| [[Hs 766T (line)]] | wt | 14.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +8.8) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.131× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 16.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 24.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -8.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 8.73 | 0 | 1 | — | [[Penfluridol (drug)]] 0.05 µM 0.0555× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 5.53 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0724× (z -9.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[RPMI-7951 (line)]] | alt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +8.6) | — |
| [[SW480 (line)]] | alt | 6.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +11.1) | — |
| [[A-172 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13566), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPESP1]] | +0.82 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[SEC24B-AS1]] | +0.75 | +0.59 / +0.62 | both halves | 7e-06 | same gene group |
| [[ZNF213-AS1]] | +0.72 | +0.59 / +0.61 | both halves | 7e-06 | same gene group |
| [[UPP2]] | +0.71 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[DARS1-AS1]] | +0.70 | +0.52 / +0.64 | both halves | 1e-05 | same gene group |
| [[NIFK-AS1]] | +0.70 | +0.61 / +0.52 | both halves | 1e-05 | same gene group |
| [[CDNF]] | +0.69 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[HLA-DMA]] | +0.69 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[LRRC8C-DT]] | +0.69 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[INTS6-AS1]] | +0.69 | +0.50 / +0.51 | both halves | 1e-05 | same gene group |
| [[ZNF460-AS1]] | +0.69 | +0.46 / +0.57 | both halves | 3e-05 | same gene group |
| [[SAP30L-AS1]] | +0.68 | +0.57 / +0.49 | both halves | 1e-05 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FKBP14-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers FKBP14-AS1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.779). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.3, 21.6); signed map (27.6, -6.2). **Vector** length 73.5, 12.2% of its response variance represented; |z| ≥ 3 in 952 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.4 | +18.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +7.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.6 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +1.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -4.0 | -4.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.8 | -10.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.6 | -6.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.6 | -9.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -4.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -3.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -3.2 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | FKBP14 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7p14.3 — chr7:29,988,600-30,027,543 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40990](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40990) · Entrez [105375215](https://www.ncbi.nlm.nih.gov/gene/105375215) · Ensembl [ENSG00000227014](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227014)

## Data

Gene col 13566: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13566); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13566, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13566]; `tensor/DDL_lfc|DDL_z.npy` [13566]; `embed/gene_vectors.npy` [13566]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13566 or target_col == 13566). Every well: [[FKBP14-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FKBP14-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
