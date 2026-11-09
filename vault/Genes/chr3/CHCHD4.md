---
symbol: "CHCHD4"
type: "gene"
col: 8710
ensembl_id: "ENSG00000163528"
name: "coiled-coil-helix-coiled-coil-helix domain containing 4"
location: "3p25.1"
module: 5
arm: "+"
pooled_cpm: 6.66
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# CHCHD4

*coiled-coil-helix-coiled-coil-helix domain containing 4* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.56× (z +9.1, q 4e-17, up in 23 of 26 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.45× (z +5.1, q 6e-05, up in 24 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.615× (z -6.7, q 1e-08, down in 24 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 1 line (RKO 0.0742×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H460 0.134×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A549 0.127×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.336×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1orf109]] (+0.72, fdr 7e-06), [[NOP16]] (+0.72, fdr 7e-06), [[TWNK]] (+0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ALDH1B1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8710.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.56×** | +9.1 | 4e-17 | 23/26 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.65×** | +8.4 | 2e-14 | 10/11 (HOP62, J82, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +5.8 | 1e-06 | 22/30 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.1 | 6e-05 | 24/42 (A549, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +4.6 | 4e-04 | 16/46 (SW480, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +4.4 | 9e-04 | 14/33 (SW1417, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.59×** | +4.2 | 0.002 | 9/21 (A-172, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.006 | 11/46 (NCI-H2347, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.023 | 16/45 (Panc 03.27, AsPC-1, …) | top dose only | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.65×** | +3.5 | 0.029 | 10/42 (MIA PaCa-2, SW1417, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.031 | 15/45 (NCI-H1792, J82, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.47×** | +3.3 | 0.052 | 10/33 (A549, LoVo, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.45×** | +3.2 | 0.069 | 8/42 (A-427, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8710.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 1 line (RKO 0.0742×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H460 0.134×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A549 0.127×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.336×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.615×** | -6.7 | 1e-08 | 24/43 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Baicalin (drug)]] 5 µM |  | **0.773×** | -3.6 | 0.100 | 11/48 (NCI-H2347, SNU-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.513× | -3.4 | 0.12 | 13/45 (SHP-77, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.734× | -3.0 | 0.35 | 3/47 (C32, SW1417, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8710. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 8.57 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 6.06 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[PANC-1 (line)]] | alt | 6.73 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -8.6) |
| [[RKO (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0742× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8710), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf109]] | +0.72 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[NOP16]] | +0.72 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[TWNK]] | +0.68 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[DHX33]] | +0.68 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[CCDC86]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[NR2C2AP]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[NIP7]] | +0.65 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[LYAR]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[NKRF]] | +0.63 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[EXOSC7]] | +0.63 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ZFYVE9]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[DDX31]] | +0.63 | +0.62 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALDH1B1]] | C | ALDH1B1 activity raises CHCHD4's level | lines that do not express ALDH1B1 (3) vs lines expressing it (47) | 2.15× lower at baseline in the lines without ALDH1B1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, CDC25A, NDC80; maybe low, not absent; its own permutation p |
| [[TSEN2]] | C | TSEN2 activity raises CHCHD4's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.05× lower at baseline in the lines without TSEN2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.647). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.9, -38.2); signed map (-1.4, -48.7). **Vector** length 50.8, 7.01% of its response variance represented; |z| ≥ 3 in 763 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.52 to 13); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.50 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.3 | +4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -2.2 | -6.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.4 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -1.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.4 | -2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.4 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil-helix-coiled-coil-helix domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:14,112,077-14,124,870 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31709, TIMM40, MIA40 |
| Gene groups (HGNC) | Coiled-coil-helix-coiled-coil-helix domain containing proteins |
| Reactome | 2 pathways, smallest: Mitochondrial protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4Q1](https://www.uniprot.org/uniprotkb/Q8N4Q1) (Mitochondrial intermembrane space import and assembly protein 40):

> Central component of a redox-sensitive mitochondrial intermembrane space import machinery which is required for the biogenesis of respiratory chain complexes. Functions as a chaperone and catalyzes the formation of disulfide bonds in substrate proteins, such as COA7, COX17, COX19, MICU1 and TIMCC/FAM136A. Required for the import and folding of small cysteine-containing proteins (small Tim) in the mitochondrial intermembrane space (IMS). Required for the import of COA7 in the IMS. Precursor …

**Summary**, from NCBI Gene [131474](https://www.ncbi.nlm.nih.gov/gene/131474):

> CHCHD4, a component of human mitochondria, belongs to a protein family whose members share 6 highly conserved cysteine residues constituting a -CXC-CX(9)C-CX(9)C- motif in the C terminus (Hofmann et al., 2005 [PubMed 16185709]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:26467](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26467) · Entrez [131474](https://www.ncbi.nlm.nih.gov/gene/131474) · UniProt [Q8N4Q1](https://www.uniprot.org/uniprotkb/Q8N4Q1) · Ensembl [ENSG00000163528](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163528)

## Data

Gene col 8710: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8710); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8710, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8710]; `tensor/DDL_lfc|DDL_z.npy` [8710]; `embed/gene_vectors.npy` [8710]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8710 or target_col == 8710). Every well: [[CHCHD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHCHD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
