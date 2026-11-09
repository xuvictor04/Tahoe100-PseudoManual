---
symbol: "MALINC1"
type: "gene"
col: 14420
ensembl_id: "ENSG00000245146"
name: "mitosis associated long intergenic non-coding RNA 1"
location: "5q31.2"
module: 35
arm: "+"
pooled_cpm: 2.32
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# MALINC1

*mitosis associated long intergenic non-coding RNA 1* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.42× (z +29.1, q 0e+00, up in 29 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.615× (z -4.7, q 0.002, down in 11 of 38 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM202-AS1]] (+0.83, fdr 7e-06), [[INTS6-AS1]] (+0.82, fdr 7e-06), [[EFCAB5]] (+0.81, fdr 7e-06).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14420.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.42×** | +29.1 | 0e+00 | 29/29 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.36×** | +13.7 | 4e-40 | 21/25 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.61×** | +13.1 | 5e-37 | 23/32 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.72×** | +12.2 | 4e-32 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.34×** | +11.7 | 2e-29 | 8/11 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.13×** | +10.6 | 3e-24 | 24/32 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.98×** | +9.7 | 2e-20 | 1/4 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.70×** | +9.6 | 5e-20 | 27/36 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.92×** | +8.9 | 3e-17 | 16/44 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.81×** | +8.1 | 2e-14 | 15/43 (SW480, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.07×** | +7.0 | 1e-10 | 14/29 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.74×** | +5.4 | 4e-06 | 10/39 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +5.1 | 2e-05 | 3/11 (SW1417, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +4.8 | 6e-05 | 3/10 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.033 | 5/42 (SW480, A549, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.044 | 5/44 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | **1.40×** | +3.0 | 0.087 | 3/32 (A-172, LoVo, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14420.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.615×** | -4.7 | 0.002 | 11/38 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.637×** | -4.3 | 0.004 | 15/39 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.642×** | -4.3 | 0.004 | 16/39 (COLO 205, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.653×** | -4.1 | 0.006 | 11/40 (SNU-1, J82, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.659×** | -4.0 | 0.007 | 11/45 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | 0.714× | -3.2 | 0.11 | 7/26 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.717× | -3.2 | 0.11 | 12/39 (LoVo, HCT15, …) | rises with dose |  |
| [[Clofarabine (drug)]] 0.05 µM |  | 0.700× | -3.2 | 0.11 | 4/35 (HEC-1-A, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14420. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 4.24 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.84× (z +11.4) | — |
| [[SW480 (line)]] | alt | 2.36 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +13.6) | — |
| [[A-172 (line)]] | wt | 2.50 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0623× (z -8.5) |
| [[A498 (line)]] | wt | 1.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 3.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.34× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 4.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.33× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 2.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.30× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 2.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +10.6) | — |
| [[LOX-IMVI (line)]] | wt | 4.30 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0804× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 2.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 2.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.54× (z +14.3) | — |
| [[SW1417 (line)]] | alt | 3.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.83× (z +10.8) | — |
| [[A-427 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.828 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.530 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.650 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.726 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14420), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM202-AS1]] | +0.83 | +0.82 / +0.64 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.82 | +0.81 / +0.63 | both halves | 7e-06 |  |
| [[EFCAB5]] | +0.81 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[PAXBP1-AS1]] | +0.81 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[SPEN-AS1]] | +0.80 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.80 | +0.82 / +0.59 | both halves | 7e-06 |  |
| [[SIAH2-AS1]] | +0.79 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[ANKHD1-DT]] | +0.79 | +0.81 / +0.60 | both halves | 7e-06 |  |
| [[CPEB2-DT]] | +0.79 | +0.79 / +0.50 | both halves | 1e-05 |  |
| [[PKN2-AS1]] | +0.78 | +0.81 / +0.36 | both halves | 1e-04 |  |
| [[LINC01090]] | +0.77 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[ITFG2-AS1]] | +0.77 | +0.76 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MALINC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HOXA-AS2]] | C | HOXA-AS2 activity raises MALINC1's level | lines that do not express HOXA-AS2 (3) vs lines expressing it (47) | 1.80× lower at baseline in the lines without HOXA-AS2 | 0.098 | ⚠ few lines (3 vs 47); across organs; also absent: HFE, COTL1, ACCS; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.866). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (10.3, 21.5); signed map (29.5, -2.4). **Vector** length 58.8, 8.65% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +29.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +13.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +9.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +12.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +13.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +3.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +2.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -3.1 | -3.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.8 | -3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.4 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.2 | -4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.0 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | mitosis associated long intergenic non-coding RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q31.2 — chr5:140,071,312-140,109,274 (-) |
| Ensembl biotype | lncRNA |
| Also known as | MA-linc1; previously LINC01024 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49009](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49009) · Entrez [100505636](https://www.ncbi.nlm.nih.gov/gene/100505636) · Ensembl [ENSG00000245146](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245146)

## Data

Gene col 14420: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14420); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14420, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14420]; `tensor/DDL_lfc|DDL_z.npy` [14420]; `embed/gene_vectors.npy` [14420]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14420 or target_col == 14420). Every well: [[MALINC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MALINC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
