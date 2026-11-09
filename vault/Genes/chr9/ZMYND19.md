---
symbol: "ZMYND19"
type: "gene"
col: 9175
ensembl_id: "ENSG00000165724"
name: "zinc finger MYND-type containing 19"
location: "9q34.3"
module: 2
arm: "+"
pooled_cpm: 4.94
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ZMYND19

*zinc finger MYND-type containing 19* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.41× (z +11.1, q 6e-26, up in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.97× (z +4.4, q 9e-04, up in 13 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.636× (z -4.0, q 0.035, down in 18 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.297×, HOP62 0.205×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TELO2]] (+0.73, fdr 7e-06), [[CCNQ]] (+0.69, fdr 1e-05), [[ADCK5]] (+0.68, fdr 7e-06); moves opposite to [[CFL2]] (-0.67, fdr 1e-05), [[DZIP3]] (-0.64, fdr 1e-05), [[ZSCAN30]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9175.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **3.41×** | +11.1 | 6e-26 | 43/47 (SW480, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.88×** | +9.6 | 3e-19 | 42/46 (SW480, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.84×** | +9.5 | 6e-19 | 42/46 (SW480, RKO, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.90×** | +8.2 | 4e-14 | 30/39 (A549, NCI-H460, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.27×** | +7.4 | 2e-11 | 28/48 (KATO III, SW480, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **2.27×** | +7.1 | 1e-10 | 14/25 (SHP-77, J82, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.07×** | +6.3 | 2e-08 | 18/36 (SW480, NCI-H460, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.97×** | +4.4 | 9e-04 | 13/34 (HEC-1-A, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.62×** | +4.3 | 1e-03 | 11/27 (MIA PaCa-2, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.62×** | +4.2 | 0.002 | 11/31 (Hs 766T, NCI-H460, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.62×** | +4.2 | 0.002 | 16/40 (SW480, RKO, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **1.63×** | +4.0 | 0.002 | 2/12 (HEC-1-A, NCI-H2347) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.55×** | +3.9 | 0.004 | 9/41 (J82, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.57×** | +3.8 | 0.007 | 12/36 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.51×** | +3.7 | 0.008 | 7/24 (SNU-423, HT-29, …) | all doses, flat | composition shift |
| [[Thymol (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.041 | 8/32 (SHP-77, RKO, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.080 | 7/45 (SW480, SW 900, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9175.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.297×, HOP62 0.205×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.636×** | -4.0 | 0.035 | 18/43 (SW48, RKO, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | 0.676× | -3.5 | 0.14 | 14/44 (A498, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.79 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9175. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 8.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -9.5) |
| [[HOP62 (line)]] | alt | 4.32 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -9.2) |
| [[SW480 (line)]] | alt | 6.42 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.51× (z +8.7) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A-172 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9175), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TELO2]] | +0.73 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[CCNQ]] | +0.69 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[ADCK5]] | +0.68 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[HIRA]] | +0.68 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[PAQR4]] | +0.68 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[AXIN1]] | +0.67 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[WDR5]] | +0.67 | +0.71 / +0.50 | both halves | 1e-05 | STRING 433 |
| [[CTU2]] | +0.67 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[VKORC1L1]] | +0.66 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[NUP85]] | +0.65 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[CDK10]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[DGCR8]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFL2]] | -0.67 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[DZIP3]] | -0.64 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[ZSCAN30]] | -0.63 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[CLCN3]] | -0.63 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[GNGT1]] | -0.62 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[SNX16]] | -0.62 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[OCIAD1]] | -0.61 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[RIPK2-DT]] | -0.60 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[PAXIP1-AS2]] | -0.60 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[TAB2]] | -0.59 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[NDUFA5]] | -0.59 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[SYNE1]] | -0.58 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.592). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-15.6, 1.6); signed map (-47.8, -15.9). **Vector** length 64.6, 10.9% of its response variance represented; |z| ≥ 3 in 840 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +3.4 | +11.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.9 | +9.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +2.6 | +9.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.2 | +8.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.7 | +3.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +2.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.5 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | -2.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | +0.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.7 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger MYND-type containing 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,582,081-137,590,512 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MIZIP |
| Gene groups (HGNC) | Zinc fingers MYND-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96E35](https://www.uniprot.org/uniprotkb/Q96E35) (Zinc finger MYND domain-containing protein 19):

> May be involved as a regulatory molecule in GPR24/MCH-R1 signaling.

**Summary**, from NCBI Gene [116225](https://www.ncbi.nlm.nih.gov/gene/116225):

> ZMYND19 is a MYND zinc finger domain-containing protein that binds to the C terminus of melanin-concentrating hormone receptor-1 (MCHR1; MIM 601751) (Bachner et al., 2002 [PubMed 12208518]), and to the N termini of alpha-tubulin (TUBA1; MIM 191110), and beta-tubulin (TUBB; MIM 191130) (Francke et al., 2005 [PubMed 16039987]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:21146](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21146) · Entrez [116225](https://www.ncbi.nlm.nih.gov/gene/116225) · UniProt [Q96E35](https://www.uniprot.org/uniprotkb/Q96E35) · Ensembl [ENSG00000165724](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165724)

## Data

Gene col 9175: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9175); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9175, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9175]; `tensor/DDL_lfc|DDL_z.npy` [9175]; `embed/gene_vectors.npy` [9175]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9175 or target_col == 9175). Every well: [[ZMYND19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZMYND19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
