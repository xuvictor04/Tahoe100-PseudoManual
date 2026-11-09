---
symbol: "CTTN-DT"
type: "gene"
col: 14474
ensembl_id: "ENSG00000246889"
name: "CTTN divergent transcript"
location: "11q13.3"
module: 15
arm: "+"
pooled_cpm: 9.77
n_lines_expressing: 50
n_dd_up: 37
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# CTTN-DT

*CTTN divergent transcript* — 11q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.44× (z +19.0, q 0e+00, up in 42 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Temsirolimus (drug)]] 0.5 µM in 1 line (HT-29 0.0749×); [[Radotinib (drug)]] 0.5 µM in 1 line (Hs 766T 0.108×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNHG10]] (+0.73, fdr 1e-05), [[GTF3C2-AS2]] (+0.72, fdr 1e-05), [[CTC-338M12.4]] (+0.68, fdr 9e-05); moves opposite to [[ISCA2]] (-0.54, fdr 1e-04), [[CREB3]] (-0.53, fdr 4e-05), [[HERC1]] (-0.52, fdr 1e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14474.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.44×** | +19.0 | 0e+00 | 42/44 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.76×** | +12.0 | 9e-31 | 41/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +10.7 | 2e-24 | 32/37 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.95×** | +10.1 | 9e-22 | 29/47 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.89×** | +9.6 | 7e-20 | 22/37 (KATO III, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +8.2 | 2e-14 | 26/46 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +8.2 | 2e-14 | 9/16 (NCI-H2347, HOP62, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +7.5 | 6e-12 | 11/25 (NCI-H2030, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +6.5 | 6e-09 | 19/45 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.3 | 2e-08 | 21/45 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.49×** | +6.1 | 7e-08 | 19/45 (Panc 03.27, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +6.0 | 9e-08 | 18/47 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +5.9 | 1e-07 | 20/47 (NCI-H1573, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.38×** | +4.9 | 4e-05 | 18/47 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.36×** | +4.7 | 1e-04 | 16/47 (HOP62, HT-29, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +4.5 | 2e-04 | 10/48 (SK-MEL-2, HT-29, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.3 | 6e-04 | 11/48 (CFPAC-1, NCI-H460, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.001 | 10/44 (HT-29, BT-474, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.002 | 13/46 (NCI-H1573, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +3.8 | 0.004 | 14/48 (HOP62, SW 900, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.006 | 5/48 (NCI-H2347, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14474.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Temsirolimus (drug)]] 0.5 µM in 1 line (HT-29 0.0749×); [[Radotinib (drug)]] 0.5 µM in 1 line (Hs 766T 0.108×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -3.1 | 0.78 | 4/48 (HCT15, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14474. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 14.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +10.3) | — |
| [[A549 (line)]] | wt | 6.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 9.01 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.108× (z -9.9) |
| [[HS-578T (line)]] | alt | 6.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 6.61 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0749× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 9.56 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.85× (z +8.8) ⚠ toxic | — |
| [[NCI-H460 (line)]] | wt | 6.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 39.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +8.5) | — |
| [[SW480 (line)]] | alt | 11.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +8.7) | — |
| [[A-172 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14474), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG10]] | +0.73 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[GTF3C2-AS2]] | +0.72 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[CTC-338M12.4]] | +0.68 | +0.36 / +0.74 | both halves | 9e-05 |  |
| [[DYNLT2]] | +0.66 | +0.32 / +0.63 | both halves | 2e-04 |  |
| [[WDR12]] | +0.65 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[RPS10-NUDT3]] | +0.63 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[YARS2]] | +0.63 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[ZBTB26]] | +0.63 | +0.28 / +0.54 | both halves | 3e-04 |  |
| [[MSTO1]] | +0.63 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[MRPS25]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[ZNF460-AS1]] | +0.62 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[VPS13B-DT]] | +0.62 | +0.43 / +0.57 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISCA2]] | -0.54 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[CREB3]] | -0.53 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[HERC1]] | -0.52 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[MSRB1]] | -0.52 | -0.29 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CTTN-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.694). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-6.8, 22.3); signed map (30.2, -17.7). **Vector** length 67.7, 10.5% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +19.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.4 | +12.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.8 | +10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +6.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.1 | +2.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.3 | +4.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.2 | +5.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.1 | +4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.8 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.1 | -0.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | CTTN divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q13.3 — chr11:70,372,246-70,398,488 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [121233926](https://www.ncbi.nlm.nih.gov/gene/121233926):

> Predicted to be involved in SRP-dependent cotranslational protein targeting to membrane, signal sequence recognition. Predicted to be part of signal recognition particle, endoplasmic reticulum targeting. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:55592](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55592) · Entrez [121233926](https://www.ncbi.nlm.nih.gov/gene/121233926) · Ensembl [ENSG00000246889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000246889)

## Data

Gene col 14474: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14474); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14474, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14474]; `tensor/DDL_lfc|DDL_z.npy` [14474]; `embed/gene_vectors.npy` [14474]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14474 or target_col == 14474). Every well: [[CTTN-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTTN-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
