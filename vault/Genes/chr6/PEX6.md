---
symbol: "PEX6"
type: "gene"
col: 4546
ensembl_id: "ENSG00000124587"
name: "peroxisomal biogenesis factor 6"
location: "6p21.1"
module: 15
arm: "+"
pooled_cpm: 9.12
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# PEX6

*peroxisomal biogenesis factor 6* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.92× (z +12.9, q 4e-35, up in 37 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.537× (z -8.7, q 2e-15, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C8orf44-SGK3]] (+0.66, fdr 1e-05), [[TIRAP]] (+0.65, fdr 1e-05), [[ZNF785]] (+0.64, fdr 1e-05); moves opposite to [[FZD5]] (-0.56, fdr 3e-05), [[MPP7]] (-0.54, fdr 1e-04), [[PADI2]] (-0.52, fdr 2e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4546.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +12.9 | 4e-35 | 37/43 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +11.2 | 1e-26 | 11/19 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +8.4 | 9e-15 | 31/45 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +7.5 | 7e-12 | 19/25 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +6.5 | 7e-09 | 18/33 (SW 900, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +6.5 | 1e-08 | 25/45 (HOP62, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +6.1 | 8e-08 | 23/44 (NCI-H2030, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +5.4 | 5e-06 | 19/39 (HT-29, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.5 | 5e-04 | 16/47 (SW1417, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +3.9 | 0.006 | 14/46 (HOP62, HepG2/C3A, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.006 | 8/46 (KATO III, SNU-423, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.006 | 17/44 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.011 | 8/46 (Panc 03.27, H4, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.012 | 11/47 (SHP-77, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.20× | +3.5 | 0.015 | 10/47 (C32, A549, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.025 | 11/46 (KATO III, SNU-423, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.064 | 6/46 (NCI-H460, HOP62, …) | inconsistent across doses | position effect removed |
| [[Darinaparsin (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.080 | 1/45 (NCI-H2347) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.080 | 5/45 (Hs 766T, SW48, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.16× | +2.9 | 0.088 | 6/46 (PANC-1, H4, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4546.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.537×** | -8.7 | 2e-15 | 27/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.649×** | -6.0 | 4e-07 | 26/45 (NCI-H23, PANC-1, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.713×** | -4.7 | 4e-04 | 19/43 (LS 180, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.747×** | -4.1 | 0.006 | 13/45 (SW480, NCI-H661, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.763×** | -3.8 | 0.017 | 10/46 (MIA PaCa-2, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Roxadustat (drug)]] 5 µM |  | 0.787× | -3.2 | 0.12 | 11/45 (AsPC-1, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4546. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 8.60 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.176× (z -8.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 14.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.286× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 4.81 | 0 | 1 | — | [[Roxadustat (drug)]] 5 µM 0.0680× (z -8.8) |
| [[H4 (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0919× (z -11.4) ⚠ cell-cycle shift, explains ~72% of this change |
| [[Hs 766T (line)]] | wt | 6.62 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.102× (z -9.6) |
| [[HS-578T (line)]] | alt | 6.95 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.108× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[LS 180 (line)]] | wt | 8.59 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0726× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 5.95 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.61× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 8.79 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.79× (z +8.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 9.88 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.115× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0751× (z -12.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 7.17 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.15× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4546), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C8orf44-SGK3]] | +0.66 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[TIRAP]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[ZNF785]] | +0.64 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[PPP1R26-AS1]] | +0.64 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[ZNF213-AS1]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[NOXRED1]] | +0.63 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[GLUD1P3]] | +0.62 | +0.40 / +0.57 | both halves | 4e-05 |  |
| [[PSMB5]] | +0.62 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[EIF4ENIF1]] | +0.62 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ZFHX2-AS1]] | +0.61 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[UQCC1]] | +0.61 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[AGAP5]] | +0.60 | +0.63 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FZD5]] | -0.56 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[MPP7]] | -0.54 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[PADI2]] | -0.52 | -0.41 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PEX6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.636). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-10.3, 21.6); signed map (4.0, -1.4). **Vector** length 65.2, 10.1% of its response variance represented; |z| ≥ 3 in 848 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.3 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +12.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +6.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.4 | +3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +8.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | -0.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -0.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -3.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.4 | -2.5 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.4 | -1.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.2 | -0.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | peroxisomal biogenesis factor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:42,963,865-42,979,181 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PXAAA1, PAF-2 |
| Gene groups (HGNC) | AAA ATPases; Peroxins |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME |
| Reactome | 2 pathways, smallest: Peroxisomal protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13608](https://www.uniprot.org/uniprotkb/Q13608) (Peroxisomal ATPase PEX6):

> Component of the PEX1-PEX6 AAA ATPase complex, a protein dislocase complex that mediates the ATP-dependent extraction of the PEX5 receptor from peroxisomal membranes, an essential step for PEX5 recycling. Specifically recognizes PEX5 monoubiquitinated at 'Cys-11', and pulls it out of the peroxisome lumen through the PEX2-PEX10-PEX12 retrotranslocation channel. Extraction by the PEX1-PEX6 AAA ATPase complex is accompanied by unfolding of the TPR repeats and release of bound cargo from PEX5.

**Summary**, from NCBI Gene [5190](https://www.ncbi.nlm.nih.gov/gene/5190):

> This gene encodes a member of the AAA (ATPases associated with diverse cellular activities) family of ATPases. This member is a predominantly cytoplasmic protein, which plays a direct role in peroxisomal protein import and is required for PTS1 (peroxisomal targeting signal 1, a C-terminal tripeptide of the sequence ser-lys-leu) receptor activity. Mutations in this gene cause peroxisome biogenesis disorders of complementation group 4 and complementation group 6. Several transcript variants …

**Accessions** — [HGNC:8859](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8859) · Entrez [5190](https://www.ncbi.nlm.nih.gov/gene/5190) · UniProt [Q13608](https://www.uniprot.org/uniprotkb/Q13608) · Ensembl [ENSG00000124587](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124587)

## Data

Gene col 4546: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4546); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4546, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4546]; `tensor/DDL_lfc|DDL_z.npy` [4546]; `embed/gene_vectors.npy` [4546]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4546 or target_col == 4546). Every well: [[PEX6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEX6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
