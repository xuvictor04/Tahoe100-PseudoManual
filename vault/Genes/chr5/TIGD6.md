---
symbol: "TIGD6"
type: "gene"
col: 8921
ensembl_id: "ENSG00000164296"
name: "tigger transposable element derived 6"
location: "5q32"
module: 10
arm: "+"
pooled_cpm: 2.33
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# TIGD6

*tigger transposable element derived 6* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.71× (z +13.8, q 2e-40, up in 22 of 29 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (A498 0.0605×); [[Palmatine (chloride) (drug)]] 5 µM in 1 line (Hs 766T 0.0887×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (PANC-1 0.138×; ⚠ toxic; cell-cycle shift, explains ~4% of this change); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0789×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM200A]] (+0.81, fdr 7e-06), [[BCDIN3D]] (+0.78, fdr 7e-06), [[ELAC1]] (+0.78, fdr 7e-06); moves opposite to [[TCF3]] (-0.68, fdr 1e-05), [[LPCAT4]] (-0.65, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8921.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.71×** | +13.8 | 2e-40 | 22/29 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.53×** | +12.9 | 2e-35 | 23/29 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.71×** | +9.8 | 3e-20 | 19/30 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.88×** | +8.8 | 3e-16 | 14/45 (NCI-H2030, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +7.3 | 4e-11 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.98×** | +6.4 | 1e-08 | 17/40 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.92×** | +6.4 | 1e-08 | 21/44 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +6.3 | 2e-08 | 1/3 (PANC-1) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.83×** | +5.9 | 2e-07 | 14/39 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +5.0 | 3e-05 | 12/27 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.83×** | +4.2 | 0.001 | 1/5 (A-172) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.53×** | +4.2 | 0.002 | 9/42 (LoVo, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.002 | 6/44 (A498, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.1 | 0.002 | 3/14 (Hs 766T, A498, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.008 | 7/47 (NCI-H460, SW1417, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +3.6 | 0.012 | 3/42 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.044 | 1/44 (SHP-77) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.059 | 6/34 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.059 | 1/45 (HOP62) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8921.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (A498 0.0605×); [[Palmatine (chloride) (drug)]] 5 µM in 1 line (Hs 766T 0.0887×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (PANC-1 0.138×; ⚠ toxic; cell-cycle shift, explains ~4% of this change); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0789×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.794× | -3.2 | 0.73 | 4/44 (HT-29, SNU-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8921. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.45 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0605× (z -9.7) |
| [[Hs 766T (line)]] | wt | 2.59 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 5 µM 0.0887× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 2.65 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0789× (z -8.5) |
| [[PANC-1 (line)]] | alt | 3.21 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.138× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~4% of this change |
| [[A-172 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8921), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM200A]] | +0.81 | +0.82 / +0.60 | both halves | 7e-06 |  |
| [[BCDIN3D]] | +0.78 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[ELAC1]] | +0.78 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[SDSL]] | +0.77 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[LINC00240]] | +0.76 | +0.81 / +0.54 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | +0.76 | +0.81 / +0.53 | both halves | 1e-05 |  |
| [[ZNF407-AS1]] | +0.76 | +0.77 / +0.55 | both halves | 1e-05 |  |
| [[ZNF747]] | +0.75 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[RBM26-AS1]] | +0.74 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[SMIM19]] | +0.73 | +0.75 / +0.47 | both halves | 2e-05 |  |
| [[ZNF181]] | +0.73 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[NAIF1]] | +0.73 | +0.74 / +0.50 | both halves | 1e-05 | STRING 481 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF3]] | -0.68 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[LPCAT4]] | -0.65 | -0.68 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TIGD6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.758). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (3.5, 13.9); signed map (12.5, -21.0). **Vector** length 43.1, 4.62% of its response variance represented; |z| ≥ 3 in 1,016 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +13.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.0 | +9.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.5 | +6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +12.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.2 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | -0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | -0.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.1 | +2.0 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -0.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -1.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.0 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -0.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -0.9 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | tigger transposable element derived 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:149,993,118-150,000,654 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761E2110 |
| Gene groups (HGNC) | Helix-turn-helix CENPB type domain family |
| Matched by | ensembl_id |

UniProt [Q17RP2](https://www.uniprot.org/uniprotkb/Q17RP2) carries no function annotation.

**Summary**, from NCBI Gene [81789](https://www.ncbi.nlm.nih.gov/gene/81789):

> The protein encoded by this gene belongs to the tigger subfamily of the pogo superfamily of DNA-mediated transposons in humans. These proteins are related to DNA transposons found in fungi and nematodes, and more distantly to the Tc1 and mariner transposases. They are also very similar to the major mammalian centromere protein B. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:18332](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18332) · Entrez [81789](https://www.ncbi.nlm.nih.gov/gene/81789) · UniProt [Q17RP2](https://www.uniprot.org/uniprotkb/Q17RP2) · Ensembl [ENSG00000164296](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164296)

## Data

Gene col 8921: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8921); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8921, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8921]; `tensor/DDL_lfc|DDL_z.npy` [8921]; `embed/gene_vectors.npy` [8921]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8921 or target_col == 8921). Every well: [[TIGD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIGD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
