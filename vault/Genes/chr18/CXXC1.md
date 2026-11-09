---
symbol: "CXXC1"
type: "gene"
col: 7844
ensembl_id: "ENSG00000154832"
name: "CXXC finger protein 1"
location: "18q21.1"
module: 2
arm: "+"
pooled_cpm: 12.06
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CXXC1

*CXXC finger protein 1* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.02× (z +8.7, q 1e-15, up in 36 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (BT-474 0.0704×); [[Simotinib (drug)]] 5 µM in 1 line (BT-474 0.110×; ⚠ toxic); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (H4 0.0887×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCF3]] (+0.63, fdr 1e-05), [[UCKL1]] (+0.62, fdr 1e-05), [[KLHL17]] (+0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF530]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7844.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.02×** | +8.7 | 1e-15 | 36/47 (NCI-H23, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.93×** | +8.2 | 6e-14 | 37/47 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.61×** | +5.9 | 6e-07 | 28/47 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +5.7 | 2e-06 | 6/48 (HEC-1-A, NCI-H2030, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +5.6 | 3e-06 | 23/47 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +5.3 | 1e-05 | 23/44 (NCI-H1573, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.1 | 3e-05 | 18/41 (SHP-77, RKO, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.1 | 3e-05 | 19/41 (KATO III, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +4.9 | 6e-05 | 22/46 (SW480, LoVo, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +4.8 | 1e-04 | 20/45 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.43×** | +4.2 | 0.002 | 17/44 (HCT15, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +4.0 | 0.004 | 12/44 (H4, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.004 | 14/47 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.51×** | +3.6 | 0.011 | 17/44 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.73×** | +3.6 | 0.013 | 12/43 (C32, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.48×** | +3.5 | 0.019 | 11/44 (NCI-H2030, AN3 CA, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.70×** | +3.4 | 0.019 | 15/48 (SHP-77, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +3.4 | 0.021 | 13/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.045 | 16/45 (SNU-423, RKO, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7844.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (BT-474 0.0704×); [[Simotinib (drug)]] 5 µM in 1 line (BT-474 0.110×; ⚠ toxic); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (H4 0.0887×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | 0.752× | -3.6 | 0.16 | 15/47 (H4, SNU-1, …) | inconsistent across doses |  |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | 0.762× | -3.4 | 0.16 | 13/46 (HS-578T, J82, …) | inconsistent across doses |  |
| [[Voriconazole (drug)]] 0.5 µM |  | 0.786× | -3.1 | 0.42 | 8/47 (RKO, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7844. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 10.8 | 0 | 2 (1 ⚠) | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0704× (z -10.5) |
| [[C-33 A (line)]] | alt | 26.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[H4 (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0887× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7844), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCF3]] | +0.63 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[UCKL1]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[KLHL17]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[INTS11]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[DPH7]] | +0.61 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[CPSF1]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 | STRING 541 |
| [[EDC4]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 487 |
| [[FCHSD1]] | +0.60 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[CHPF2]] | +0.59 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[POLRMT]] | +0.59 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[USP35]] | +0.59 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[E2F4]] | +0.58 | +0.54 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF530]] | B | ZNF530 activity lowers CXXC1's level | lines that do not express ZNF530 (9) vs lines expressing it (41) | 1.46× higher at baseline in the lines without ZNF530 | 0.014 | ⚠ within organs, on part of the lines; also absent: ZNF134, ENSG00000286964, SIX1 |
| [[XKR8]] | B | XKR8 activity lowers CXXC1's level | lines that do not express XKR8 (6) vs lines expressing it (44) | 1.33× higher at baseline in the lines without XKR8 | 0.087 | ⚠ within organs, on part of the lines; also absent: MORC4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.595). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-7.8, -24.6); signed map (-44.1, -11.3). **Vector** length 67.8, 11.3% of its response variance represented; |z| ≥ 3 in 832 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.5 | +5.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.4 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +3.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.9 | +2.0 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.6 | +2.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.5 | +3.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.3 | +4.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.1 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +0.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.4 | -0.7 |
|  | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -3.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.4 | -0.3 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | CXXC finger protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:50,282,343-50,287,839 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HsT2645, PCCX1, hCGBP, PHF18, CGBP, SPP1, CFP1, ZCGPC1 |
| Gene groups (HGNC) | PHD finger proteins; Zinc fingers CXXC-type |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 8 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; XBP1(S) activates chaperone genes; IRE1alpha activates chaperones |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0U4](https://www.uniprot.org/uniprotkb/Q9P0U4) (CXXC-type zinc finger protein 1):

> Transcriptional activator that exhibits a unique DNA binding specificity for CpG unmethylated motifs with a preference for CpGG.

**Summary**, from NCBI Gene [30827](https://www.ncbi.nlm.nih.gov/gene/30827):

> This gene encodes a protein that functions as a transcriptional activator that binds specifically to non-methylated CpG motifs through its CXXC domain. The protein is a component of the SETD1 complex, regulates gene expression and is essential for vertebrate development. [provided by RefSeq, Sep 2015]

**Accessions** — [HGNC:24343](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24343) · Entrez [30827](https://www.ncbi.nlm.nih.gov/gene/30827) · UniProt [Q9P0U4](https://www.uniprot.org/uniprotkb/Q9P0U4) · Ensembl [ENSG00000154832](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154832)

## Data

Gene col 7844: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7844); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7844, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7844]; `tensor/DDL_lfc|DDL_z.npy` [7844]; `embed/gene_vectors.npy` [7844]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7844 or target_col == 7844). Every well: [[CXXC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CXXC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
