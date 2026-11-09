---
symbol: "SYCE1L"
type: "gene"
col: 12945
ensembl_id: "ENSG00000205078"
name: "synaptonemal complex central element protein 1 like"
location: "16q23.1"
module: 38
arm: "+"
pooled_cpm: 5.25
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# SYCE1L

*synaptonemal complex central element protein 1 like* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.68× (z +7.3, q 2e-10, up in 22 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.485× (z -7.2, q 3e-10, down in 26 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP2A1]] (+0.81, fdr 7e-06), [[TTLL3]] (+0.74, fdr 7e-06), [[ISY1-RAB43]] (+0.74, fdr 7e-06); moves opposite to [[IDH3A]] (-0.56, fdr 2e-05), [[RAB14]] (-0.56, fdr 3e-05), [[MBTPS2]] (-0.56, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GP6-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12945.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +7.3 | 2e-10 | 22/39 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +5.2 | 5e-05 | 10/24 (NCI-H2030, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +4.2 | 0.004 | 5/12 (NCI-H2030, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +4.2 | 0.004 | 7/41 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[TAK-733 (drug)]] 0.05 µM |  | **1.46×** | +3.5 | 0.049 | 5/44 (J82, PANC-1, …) | inconsistent across doses |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.37× | +3.1 | 0.15 | 9/39 (LOX-IMVI, CFPAC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.38× | +3.1 | 0.15 | 8/26 (CFPAC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Belzutifan (drug)]] 5 µM |  | 1.81× | +3.1 | 0.15 | 4/27 (NCI-H2030, PANC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12945.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.485×** | -7.2 | 3e-10 | 26/44 (SW480, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.496×** | -7.0 | 7e-10 | 25/46 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.520×** | -6.5 | 1e-08 | 23/37 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.512×** | -6.4 | 2e-08 | 22/43 (NCI-H1573, J82, …) | two highest doses | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.600×** | -5.1 | 4e-05 | 17/41 (BT-474, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.707×** | -4.9 | 8e-05 | 21/35 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.606×** | -4.8 | 1e-04 | 18/37 (J82, SW 900, …) | top dose only |  |
| [[Erlotinib (drug)]] 5 µM |  | **0.672×** | -3.8 | 0.009 | 14/40 (H4, KATO III, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.684×** | -3.8 | 0.009 | 13/42 (NCI-H460, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.687×** | -3.8 | 0.010 | 14/42 (RKO, BT-474, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | **0.694×** | -3.5 | 0.021 | 10/41 (KATO III, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.685×** | -3.5 | 0.021 | 5/46 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.724×** | -3.2 | 0.054 | 14/36 (J82, A-427, …) | all doses, flat |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.718×** | -3.1 | 0.089 | 6/44 (CFPAC-1, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12945. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 4.74 | 0 | 2 (1 ⚠) | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0818× (z -9.4) |
| [[A-427 (line)]] | wt | 4.68 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0775× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HEC-1-A (line)]] | alt | 3.79 | 0 | 1 | — | [[Penfluridol (drug)]] 5 µM 0.0729× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 5.58 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0244× (z -10.0) |
| [[LoVo (line)]] | wt | 3.65 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.103× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 3.38 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0613× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0921× (z -9.8) |
| [[SW480 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12945), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP2A1]] | +0.81 | +0.79 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[TTLL3]] | +0.74 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[ISY1-RAB43]] | +0.74 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[MON1B]] | +0.69 | +0.67 / +0.69 | both halves | 7e-06 | STRING 543; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SRRM5]] | +0.66 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[RABGEF1]] | +0.66 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[LINC00672]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[MASP2]] | +0.65 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[HYAL1]] | +0.65 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[SMIM41]] | +0.65 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[CD200R1]] | +0.64 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[TFAP2E]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[BIN3]] | +0.64 | +0.56 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDH3A]] | -0.56 | -0.68 / -0.48 | both halves | 2e-05 |  |
| [[RAB14]] | -0.56 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[MBTPS2]] | -0.56 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[AKAP11]] | -0.55 | -0.55 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GP6-AS1]] | B | GP6-AS1 activity raises SYCE1L's level | lines that do not express GP6-AS1 (13) vs lines expressing it (37) | 1.39× lower at baseline in the lines without GP6-AS1 | 0.080 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.706). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.9, -20.0); signed map (11.5, 12.0). **Vector** length 66.0, 11.1% of its response variance represented; |z| ≥ 3 in 806 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +4.2 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.9 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +1.5 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.8 | +3.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.0 | -7.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.5 | -6.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | -7.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -2.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.6 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | synaptonemal complex central element protein 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:77,199,408-77,213,215 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRP2 |
| Matched by | ensembl_id |

**Function**, from UniProt [A8MT33](https://www.uniprot.org/uniprotkb/A8MT33) (Synaptonemal complex central element protein 1-like):

> May be involved in meiosis.

**Summary**, from NCBI Gene [100130958](https://www.ncbi.nlm.nih.gov/gene/100130958):

> Predicted to be involved in synaptonemal complex assembly. Predicted to be active in synaptonemal complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:37236](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37236) · Entrez [100130958](https://www.ncbi.nlm.nih.gov/gene/100130958) · UniProt [A8MT33](https://www.uniprot.org/uniprotkb/A8MT33) · Ensembl [ENSG00000205078](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205078)

## Data

Gene col 12945: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12945); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12945, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12945]; `tensor/DDL_lfc|DDL_z.npy` [12945]; `embed/gene_vectors.npy` [12945]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12945 or target_col == 12945). Every well: [[SYCE1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYCE1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
