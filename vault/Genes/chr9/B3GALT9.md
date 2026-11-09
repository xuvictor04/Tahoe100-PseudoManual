---
symbol: "B3GALT9"
type: "gene"
col: 13212
ensembl_id: "ENSG00000214654"
name: "beta-1,3-galactosyltransferase 9"
location: "9q33.2"
module: 16
arm: "+"
pooled_cpm: 2.06
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# B3GALT9

*beta-1,3-galactosyltransferase 9* — 9q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 3.14× (z +9.0, q 8e-17, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.54× (z +8.0, q 4e-13, up in 30 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.446× (z -6.9, q 3e-09, down in 23 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HERPUD2-AS1]] (+0.72, fdr 7e-06), [[ZFP41]] (+0.72, fdr 7e-06), [[RAB4A-AS1]] (+0.70, fdr 7e-06); moves opposite to [[COG7]] (-0.62, fdr 1e-05), [[C9orf153]] (-0.61, fdr 2e-05), [[C12orf57]] (-0.60, fdr 9e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13212.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.14×** | +9.0 | 8e-17 | 0/1 | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.54×** | +8.0 | 4e-13 | 30/43 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +7.7 | 3e-12 | 0/0 | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.28×** | +7.1 | 2e-10 | 20/41 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.79×** | +7.1 | 2e-10 | 13/41 (HEC-1-A, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.03×** | +6.1 | 1e-07 | 5/10 (HEC-1-A, J82, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.90×** | +5.5 | 4e-06 | 16/42 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +5.0 | 3e-05 | 8/44 (A549, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +4.2 | 0.002 | 1/13 (SW480) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +4.2 | 0.002 | 7/25 (SHP-77, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.57×** | +3.8 | 0.006 | 2/38 (Hs 766T, LoVo) | inconsistent across doses | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.53×** | +3.6 | 0.014 | 1/15 (PANC-1) | inconsistent across doses | low cells (technical?) |
| [[Larotrectinib (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.014 | 3/40 (LoVo, BT-474, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.50×** | +3.5 | 0.021 | 5/37 (A-172, NCI-H460, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.055 | 3/44 (KATO III, HCT15, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.44×** | +3.1 | 0.061 | 2/43 (KATO III, A549) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13212.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.446×** | -6.9 | 3e-09 | 23/37 (NCI-H23, PANC-1, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.466×** | -6.5 | 2e-08 | 19/46 (COLO 205, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.527×** | -5.5 | 8e-06 | 17/38 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.546×** | -4.9 | 1e-04 | 15/31 (KATO III, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.577×** | -4.7 | 3e-04 | 17/34 (KATO III, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.580×** | -4.7 | 3e-04 | 12/45 (H4, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.599×** | -4.4 | 9e-04 | 14/44 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.619×** | -4.1 | 0.003 | 15/38 (LS 180, SK-MEL-2, …) | rises with dose |  |
| [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM |  | **0.688×** | -3.2 | 0.085 | 4/43 (H4, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13212. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 3.77 | 0 | 2 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0583× (z -10.0) |
| [[A-172 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.644 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.729 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.826 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.988 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.854 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13212), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERPUD2-AS1]] | +0.72 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[ZFP41]] | +0.72 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[RAB4A-AS1]] | +0.70 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[GGACT]] | +0.69 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[ZFP62]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[SAYSD1]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[PIGM]] | +0.65 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[PLPP6]] | +0.65 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[TMEM185B]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[CEP41]] | +0.64 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[IQCH]] | +0.63 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[TTC30A]] | +0.63 | +0.63 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG7]] | -0.62 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[C9orf153]] | -0.61 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[C12orf57]] | -0.60 | -0.36 / -0.63 | both halves | 9e-05 |  |
| [[TRNAU1AP]] | -0.59 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[TNXB]] | -0.58 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[EOGT-DT]] | -0.57 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[PMS2P4-1]] | -0.57 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[VDAC1P8]] | -0.56 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[NARF]] | -0.56 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[KLC4]] | -0.55 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[PHKG1]] | -0.55 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[GNRH1]] | -0.54 | -0.51 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises B3GALT9's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.588). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.2, 17.9); signed map (-1.2, -31.4). **Vector** length 40.5, 4.63% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.3 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +1.9 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.1 | +2.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.0 | +0.9 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -2.5 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.5 | -5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -4.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.6 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -4.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.9 | -0.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | beta-1,3-galactosyltransferase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2 — chr9:120,792,403-120,801,787 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously B3GNT10 |
| Gene groups (HGNC) | Beta 3-glycosyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [A8MXE2](https://www.uniprot.org/uniprotkb/A8MXE2) (Beta-1,3-galactosyltransferase 9):

> Putative glycosyltransferase that could catalyze the transfer of galactose residues from UDP-alpha-D-galactose.

**Summary**, from NCBI Gene [100288842](https://www.ncbi.nlm.nih.gov/gene/100288842):

> Predicted to enable glycosyltransferase activity. Predicted to be involved in glycoprotein biosynthetic process and lipid metabolic process. Predicted to be located in membrane. Predicted to be active in Golgi membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:53652](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53652) · Entrez [100288842](https://www.ncbi.nlm.nih.gov/gene/100288842) · UniProt [A8MXE2](https://www.uniprot.org/uniprotkb/A8MXE2) · Ensembl [ENSG00000214654](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214654)

## Data

Gene col 13212: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13212); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13212, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13212]; `tensor/DDL_lfc|DDL_z.npy` [13212]; `embed/gene_vectors.npy` [13212]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13212 or target_col == 13212). Every well: [[B3GALT9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B3GALT9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
