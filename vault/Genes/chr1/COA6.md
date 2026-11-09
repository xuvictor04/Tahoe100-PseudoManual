---
symbol: "COA6"
type: "gene"
col: 9623
ensembl_id: "ENSG00000168275"
name: "cytochrome c oxidase assembly factor 6"
location: "1q42.2"
module: 89
arm: "+"
pooled_cpm: 20.33
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# COA6

*cytochrome c oxidase assembly factor 6* — 1q42.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.40× (z +8.4, q 2e-14, up in 40 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 2.07× (z +7.0, q 5e-10, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.545× (z -5.8, q 3e-06, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A17]] (+0.76, fdr 7e-06), [[NGDN]] (+0.71, fdr 3e-05), [[ZCCHC10]] (+0.67, fdr 1e-05); moves opposite to [[CSRP1]] (-0.66, fdr 1e-05), [[MYH9]] (-0.63, fdr 1e-05), [[COTL1]] (-0.60, fdr 3e-05).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9623.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.40×** | +8.4 | 2e-14 | 40/46 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +7.1 | 4e-10 | 38/44 (PANC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.07×** | +7.0 | 5e-10 | 40/47 (LS 180, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +6.5 | 1e-08 | 39/47 (LoVo, SHP-77, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.93×** | +6.3 | 3e-08 | 42/47 (LS 180, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.96×** | +6.1 | 9e-08 | 38/48 (LS 180, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.88×** | +6.1 | 9e-08 | 33/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.75×** | +5.4 | 5e-06 | 31/45 (NCI-H1792, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.70×** | +5.1 | 2e-05 | 32/47 (NCI-H460, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.8 | 9e-05 | 29/47 (SW 900, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.68×** | +4.3 | 8e-04 | 24/40 (A-427, LoVo, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.53×** | +4.1 | 0.002 | 24/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.53×** | +4.0 | 0.003 | 18/30 (A-172, NCI-H460, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.18×** | +3.9 | 0.004 | 24/48 (LS 180, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.006 | 23/48 (Panc 03.27, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.037 | 19/48 (H4, NCI-H1792, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.046 | 20/47 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.046 | 21/46 (RKO, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9623.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.545×** | -5.8 | 3e-06 | 32/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.601×** | -4.9 | 3e-04 | 28/47 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.608×** | -4.8 | 3e-04 | 29/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.729× | -3.0 | 0.31 | 19/47 (A498, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9623. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 55.1 | 6 (5 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 5.17× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 4.99× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.321× (z -9.0) |
| [[HOP62 (line)]] | alt | 13.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.191× (z -9.2) |
| [[A-172 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9623), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A17]] | +0.76 | +0.66 / +0.67 | both halves | 7e-06 | pathway: Protein localization |
| [[NGDN]] | +0.71 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[ZCCHC10]] | +0.67 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[PSMB5]] | +0.67 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[TEFM]] | +0.65 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[ELMOD3]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[YBEY]] | +0.65 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[TMEM79]] | +0.64 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[MRPL32]] | +0.64 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[ZBTB8OS]] | +0.64 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[ALKBH4]] | +0.64 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[CCDC142]] | +0.64 | +0.45 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSRP1]] | -0.66 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[MYH9]] | -0.63 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[COTL1]] | -0.60 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[ACTN4]] | -0.59 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[PITPNM1]] | -0.56 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[RALY]] | -0.56 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[NCOR2]] | -0.56 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[TTLL12]] | -0.55 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[CORO1C]] | -0.55 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[PLEC]] | -0.55 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[ECE1]] | -0.55 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[ZMIZ2]] | -0.55 | -0.45 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises COA6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.713). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-45.4, 9.0); signed map (-5.7, -5.3). **Vector** length 74.1, 18.1% of its response variance represented; |z| ≥ 3 in 790 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.3 | +3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.7 | +6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.5 | +7.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.4 | +7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +6.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +0.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.9 | +2.4 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -4.1 | -5.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | -4.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.6 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.0 | +1.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | -3.0 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | +0.1 |
|  | [[Roxadustat (drug)]] 5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase assembly factor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.2 — chr1:234,373,456-234,385,080 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C1orf31 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 2 pathways, smallest: Mitochondrial protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JTJ3](https://www.uniprot.org/uniprotkb/Q5JTJ3) (Cytochrome c oxidase assembly factor 6 homolog):

> Involved in the maturation of the mitochondrial respiratory chain complex IV subunit MT-CO2/COX2. Thereby, may regulate early steps of complex IV assembly. Mitochondrial respiratory chain complex IV or cytochrome c oxidase is the component of the respiratory chain that catalyzes the transfer of electrons from intermembrane space cytochrome c to molecular oxygen in the matrix and as a consequence contributes to the proton gradient involved in mitochondrial ATP synthesis. May also be required for …

**Summary**, from NCBI Gene [388753](https://www.ncbi.nlm.nih.gov/gene/388753):

> This gene encodes a member of the cytochrome c oxidase subunit 6B family. The encoded protein associates with cytochrome c oxidase may act has an cytochrome c oxidase mitochondrial respiratory complex VI assembly factor. Mutations in this gene may be associated with fatal infantile cardiomyopathy. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Sep 2014]

**Accessions** — [HGNC:18025](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18025) · Entrez [388753](https://www.ncbi.nlm.nih.gov/gene/388753) · UniProt [Q5JTJ3](https://www.uniprot.org/uniprotkb/Q5JTJ3) · Ensembl [ENSG00000168275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168275)

## Data

Gene col 9623: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9623); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9623, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9623]; `tensor/DDL_lfc|DDL_z.npy` [9623]; `embed/gene_vectors.npy` [9623]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9623 or target_col == 9623). Every well: [[COA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
