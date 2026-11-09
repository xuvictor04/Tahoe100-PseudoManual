---
symbol: "MRPL12"
type: "gene"
col: 15395
ensembl_id: "ENSG00000262814"
name: "mitochondrial ribosomal protein L12"
location: "17q25.3"
module: 58
arm: "+"
pooled_cpm: 8.5
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# MRPL12

*mitochondrial ribosomal protein L12* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.61× (z +7.7, q 5e-12, up in 30 of 30 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Arbutin (drug)]] 5 µM: 1.81× (z +3.4, q 0.041, up in 20 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.532× (z -5.4, q 4e-05, down in 30 of 42 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMM13]] (+0.74, fdr 1e-05), [[ANTKMT]] (+0.71, fdr 7e-05), [[DCTPP1]] (+0.71, fdr 1e-05); moves opposite to [[GNAS]] (-0.60, fdr 6e-05), [[ZNF213-AS1]] (-0.57, fdr 1e-04), [[CROCC]] (-0.56, fdr 0.002, ⚠ one half only (not replicated)), [[SEC24B-AS1]] (-0.55, fdr 3e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[NDUFAF8]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15395.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **3.61×** | +7.7 | 5e-12 | 30/30 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **3.21×** | +6.8 | 4e-09 | 16/17 (A498, HT-29, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.54×** | +5.2 | 3e-05 | 19/25 (SW480, NCI-H2347, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.16×** | +4.6 | 5e-04 | 35/45 (SW480, NCI-H2030, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **2.14×** | +4.6 | 5e-04 | 26/35 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.56×** | +3.8 | 0.014 | 25/46 (Hs 766T, Panc 03.27, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **1.86×** | +3.6 | 0.026 | 19/36 (NCI-H1792, A549, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.81×** | +3.4 | 0.041 | 20/44 (COLO 205, SNU-423, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **1.73×** | +3.3 | 0.061 | 17/43 (NCI-H460, NCI-H1792, …) | top dose only | position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +3.2 | 0.071 | 18/43 (LoVo, SW480, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | 2.66× | +3.1 | 0.10 | 13/36 (NCI-H2347, J82, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15395.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.532×** | -5.4 | 4e-05 | 30/42 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.554×** | -5.1 | 1e-04 | 29/41 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.287×** | -3.9 | 0.015 | 26/45 (NCI-H460, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.324×** | -3.6 | 0.052 | 21/44 (SNU-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.380× | -3.1 | 0.24 | 17/48 (LoVo, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.70 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15395. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 7.37 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 17.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -9.6) |
| [[SW480 (line)]] | alt | 11.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -8.6) |
| [[A-172 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15395), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 15 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM13]] | +0.74 | +0.54 / +0.81 | both halves | 1e-05 |  |
| [[ANTKMT]] | +0.71 | +0.37 / +0.71 | both halves | 7e-05 |  |
| [[DCTPP1]] | +0.71 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[HAUS7]] | +0.71 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[CISD3]] | +0.70 | +0.52 / +0.73 | both halves | 1e-05 | STRING 540 |
| [[TMEM147]] | +0.69 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[ATP5MC1]] | +0.67 | +0.57 / +0.65 | both halves | 9e-06 | STRING 596 |
| [[HSD17B10]] ⚠ | +0.67 | +0.56 / +0.70 | both halves | 1e-05 | pathway: Mitochondrial protein degradation; STRING 490; ⚠ in the vector space only through flagged drug-doses |
| [[POLR3K]] | +0.67 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[MRPL14]] | +0.66 | +0.22 / +0.66 | both halves | 6e-04 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 932 |
| [[MRPL24]] | +0.66 | +0.59 / +0.70 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 996 |
| [[ATP5F1D]] ⚠ | +0.66 | +0.36 / +0.66 | both halves | 1e-04 | STRING 958; ⚠ in the vector space only through flagged drug-doses |
| [[TOMM22]] | +0.65 | +0.53 / +0.69 | both halves | 1e-05 | STRING 648 |
| [[PUSL1]] | +0.65 | +0.31 / +0.63 | both halves | 2e-04 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.60 | -0.38 / -0.59 | both halves | 6e-05 |  |
| [[ZNF213-AS1]] | -0.57 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[CROCC]] | -0.56 | -0.12 / -0.52 | ⚠ one half (not replicated) | 0.002 |  |
| [[SEC24B-AS1]] | -0.55 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[CHD3]] | -0.55 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[LHFPL3]] | -0.54 | -0.26 / -0.37 | both halves | 4e-04 |  |
| [[RNF11]] | -0.54 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[ZNF451-AS1]] | -0.54 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[SNHG22]] | -0.54 | -0.13 / -0.54 | ⚠ one half (not replicated) | 0.002 |  |
| [[USP34-DT]] | -0.54 | -0.32 / -0.37 | both halves | 1e-04 |  |
| [[C14orf28]] | -0.53 | -0.40 / -0.44 | both halves | 4e-05 |  |
| [[CSDE1]] | -0.53 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[SDF4]] | -0.53 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[KIAA1191]] | -0.53 | -0.39 / -0.53 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDUFAF8]] | C | MRPL12's natural level strengthens NDUFAF8's drug response | MRPL12's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.10; direction clear | 0.037 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-48.4, -15.1); signed map (-37.7, -27.5). **Vector** length 59.5, 13.7% of its response variance represented; |z| ≥ 3 in 577 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *oxidative phosphorylation* (hallmark, mean cos +0.51 to 12); *Cristae formation* (reactome, mean cos +0.63 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.7 | +4.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.2 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +0.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.3 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -5.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | -3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -2.1 | +5.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.9 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,703,367-81,707,517 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRPL7/L12, MRPL7, bL12m; previously RPML12 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 7 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial protein degradation; Mitochondrial translation elongation |
| Matched by | ensembl_id |

**Function**, from UniProt [P52815](https://www.uniprot.org/uniprotkb/P52815) (Large ribosomal subunit protein bL12m):

> As a component of the mitochondrial large ribosomal subunit, plays a role in mitochondrial translation. When present in mitochondria as a free protein not associated with the ribosome, associates with mitochondrial RNA polymerase POLRMT to activate transcription. Required for POLRMT stability.

**Summary**, from NCBI Gene [6182](https://www.ncbi.nlm.nih.gov/gene/6182):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:10378](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10378) · Entrez [6182](https://www.ncbi.nlm.nih.gov/gene/6182) · UniProt [P52815](https://www.uniprot.org/uniprotkb/P52815) · Ensembl [ENSG00000262814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000262814)

## Data

Gene col 15395: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15395); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15395, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15395]; `tensor/DDL_lfc|DDL_z.npy` [15395]; `embed/gene_vectors.npy` [15395]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15395 or target_col == 15395). Every well: [[MRPL12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
