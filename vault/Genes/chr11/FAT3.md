---
symbol: "FAT3"
type: "gene"
col: 9108
ensembl_id: "ENSG00000165323"
name: "FAT atypical cadherin 3"
location: "11q14.3"
module: 150
arm: "+"
pooled_cpm: 3.96
n_lines_expressing: 47
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# FAT3

*FAT atypical cadherin 3* — 11q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.52× (z +21.8, q 0e+00, up in 20 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0692×; ⚠ cell-cycle shift, explains ~25% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GALNTL6]] (+0.79, fdr 7e-06), [[LINC02208]] (+0.79, fdr 7e-06), [[LRRC4C]] (+0.77, fdr 7e-06).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[AFF2]] → it (grade B ⚠); 2 go from it, the strongest it → [[CCDC3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9108.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.52×** | +21.8 | 0e+00 | 20/25 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.33×** | +15.1 | 0e+00 | 8/13 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.12×** | +14.5 | 3e-45 | 18/28 (CFPAC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.60×** | +13.2 | 8e-38 | 1/4 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.90×** | +11.3 | 1e-27 | 1/5 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.03×** | +10.0 | 1e-21 | 22/35 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.87×** | +8.0 | 1e-13 | 18/37 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.02×** | +6.3 | 2e-08 | 11/25 (SW 900, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +5.6 | 1e-06 | 9/21 (J82, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +5.5 | 2e-06 | 14/29 (A-172, HS-578T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +5.4 | 3e-06 | 8/26 (J82, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.1 | 1e-05 | 10/38 (A498, J82, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +4.9 | 5e-05 | 5/15 (NCI-H1573, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +4.5 | 2e-04 | 11/30 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.43×** | +4.2 | 0.001 | 1/8 (A498) | top dose only | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.030 | 1/25 (HEC-1-A) | inconsistent across doses | position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.64×** | +3.2 | 0.041 | 0/19 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.046 | 2/26 (SNU-423, A-427) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +2.9 | 0.077 | 5/32 (CFPAC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9108.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0692×; ⚠ cell-cycle shift, explains ~25% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | 0.791× | -3.0 | 0.82 | 10/41 (C-33 A, J82, …) | rises with dose | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9108. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 1.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.7× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 1.91 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.7× (z +12.1) | — |
| [[HEC-1-A (line)]] | alt | 1.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.4× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 5.51 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0692× (z -8.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[PANC-1 (line)]] | alt | 1.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +10.2) | — |
| [[SW480 (line)]] | alt | 1.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +9.6) | — |
| [[A-172 (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.950 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.868 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9108), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNTL6]] | +0.79 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[LINC02208]] | +0.79 | +0.64 / +0.80 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.77 | +0.62 / +0.79 | both halves | 7e-06 |  |
| [[LUZP2]] | +0.75 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[COL21A1]] | +0.75 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[GRIA4]] | +0.74 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[LINC01414]] | +0.74 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[CLVS1]] | +0.73 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[THSD7B]] | +0.73 | +0.57 / +0.74 | both halves | 1e-05 |  |
| [[C8orf34]] | +0.72 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[ATP8A2]] | +0.72 | +0.60 / +0.79 | both halves | 7e-06 |  |
| [[CNBD1]] | +0.72 | +0.59 / +0.79 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AFF2]] | B | AFF2 activity raises FAT3's level | lines that do not express AFF2 (25) vs lines expressing it (25) | 1.79× lower at baseline in the lines without AFF2 | 0.012 | ⚠ within organs, on part of the lines; also absent: KIF1A, TMEM163, LINC02315; maybe low, not absent |
| [[LINC02492]] | B | LINC02492 activity raises FAT3's level | lines that do not express LINC02492 (32) vs lines expressing it (18) | 2.16× lower at baseline in the lines without LINC02492 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000260289, ENSG00000254337, RHOJ; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers FAT3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC3]] | C | FAT3 activity lowers CCDC3's level | lines that do not express FAT3 (3) vs lines expressing it (47) | 3.18× higher at baseline in the lines without FAT3 | 0.066 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLN2, CCDC144NL-1, ARHGAP15; maybe low, not absent |
| [[LINC01117]] | C | FAT3 activity raises LINC01117's level | lines that do not express FAT3 (3) vs lines expressing it (47) | 2.87× lower at baseline in the lines without FAT3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLN2, CCDC144NL-1, ARHGAP15; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.835). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.8, 29.1); signed map (34.1, 15.3). **Vector** length 44.2, 5.96% of its response variance represented; |z| ≥ 3 in 881 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +21.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.1 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.7 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.7 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +5.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +0.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.7 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | FAT atypical cadherin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.3 — chr11:92,224,818-92,896,473 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1989, CDHF15, CDHR10 |
| Gene groups (HGNC) | Cadherin related |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDW7](https://www.uniprot.org/uniprotkb/Q8TDW7) (Protocadherin Fat 3):

> May play a role in the interactions between neurites derived from specific subsets of neurons during development.

**Summary**, from NCBI Gene [120114](https://www.ncbi.nlm.nih.gov/gene/120114):

> Predicted to enable calcium ion binding activity. Predicted to be involved in cell-cell adhesion mediated by cadherin. Predicted to act upstream of or within several processes, including negative regulation of dendrite development; neuron migration; and retina layer formation. Predicted to be located in dendrite and membrane. Predicted to be active in adherens junction and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23112](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23112) · Entrez [120114](https://www.ncbi.nlm.nih.gov/gene/120114) · UniProt [Q8TDW7](https://www.uniprot.org/uniprotkb/Q8TDW7) · Ensembl [ENSG00000165323](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165323)

## Data

Gene col 9108: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9108); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9108, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9108]; `tensor/DDL_lfc|DDL_z.npy` [9108]; `embed/gene_vectors.npy` [9108]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9108 or target_col == 9108). Every well: [[FAT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
