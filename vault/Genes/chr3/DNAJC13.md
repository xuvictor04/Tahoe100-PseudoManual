---
symbol: "DNAJC13"
type: "gene"
col: 6145
ensembl_id: "ENSG00000138246"
name: "DnaJ heat shock protein family (Hsp40) member C13"
location: "3q22.1"
module: 25
arm: "+"
pooled_cpm: 108.2
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 6
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# DNAJC13

*DnaJ heat shock protein family (Hsp40) member C13* — 3q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.21× (z +5.1, q 2e-04, up in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.28× (z +4.5, q 0.002, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.806× (z -5.7, q 7e-06, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX15]] (+0.65, fdr 7e-06), [[MBTPS2]] (+0.63, fdr 2e-05), [[VPS35]] (+0.63, fdr 7e-06); moves opposite to [[MIDN]] (-0.64, fdr 1e-05), [[ZBTB7A]] (-0.61, fdr 2e-05), [[SLC66A2]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6145.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.21×** | +5.1 | 2e-04 | 28/48 (HT-29, KATO III, …) | rises with dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +4.5 | 0.002 | 25/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.68×** | +3.8 | 0.027 | 24/49 (A-172, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.029 | 22/48 (A-172, C-33 A, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.058 | 20/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.21 | 18/48 (A-172, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6145.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.806×** | -5.7 | 7e-06 | 31/48 (HOP62, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.736×** | -5.5 | 1e-05 | 37/47 (C-33 A, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Thymol (drug)]] 0.5 µM |  | **0.769×** | -4.8 | 3e-04 | 31/48 (A498, A-427, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.795×** | -4.2 | 0.004 | 27/49 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.818×** | -3.7 | 0.020 | 22/48 (A-172, NCI-H23, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.693×** | -3.6 | 0.029 | 26/48 (HCT15, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.874× | -3.6 | 0.031 | 6/49 (RPMI-7951, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.838× | -3.3 | 0.069 | 21/48 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.848× | -3.1 | 0.13 | 18/48 (C32, A-172, …) | all doses, stronger at high dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.849× | -3.0 | 0.13 | 18/48 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6145. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 68.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.573× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 78.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -9.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[C-33 A (line)]] | alt | 96.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[C32 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[KATO III (line)]] | alt | 113 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 114 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 60.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[PANC-1 (line)]] | alt | 124 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +9.2) | — |
| [[RKO (line)]] | wt | 80.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 156 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 91.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 138 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 82.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 136 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 113 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 114 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 73.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 72.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 102 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6145), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX15]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[MBTPS2]] | +0.63 | +0.49 / +0.69 | both halves | 2e-05 |  |
| [[VPS35]] | +0.63 | +0.68 / +0.63 | both halves | 7e-06 | same gene group; STRING 937 |
| [[VPS26A]] | +0.63 | +0.51 / +0.69 | both halves | 1e-05 | STRING 676 |
| [[UBQLN1]] | +0.61 | +0.45 / +0.73 | both halves | 3e-05 |  |
| [[EIF4H]] | +0.61 | +0.40 / +0.74 | both halves | 5e-05 |  |
| [[STX16]] | +0.61 | +0.42 / +0.70 | both halves | 4e-05 |  |
| [[EXOC5]] | +0.60 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[IARS2]] | +0.59 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[STRADB]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[GNS]] | +0.59 | +0.34 / +0.71 | both halves | 1e-04 |  |
| [[EIF2D]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIDN]] | -0.64 | -0.57 / -0.68 | both halves | 1e-05 |  |
| [[ZBTB7A]] | -0.61 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[SLC66A2]] | -0.57 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[IER5]] | -0.55 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[ELL]] | -0.55 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[RABGEF1P1]] | -0.54 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[ATG101]] | -0.54 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[KLF16]] | -0.53 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[SLC25A25]] | -0.53 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[ACAP1]] | -0.52 | -0.36 / -0.61 | both halves | 1e-04 |  |
| [[ISG20L2]] | -0.52 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[NTMT1]] | -0.51 | -0.48 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises DNAJC13's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.658). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-24.1, -16.6); signed map (-17.7, -35.2). **Vector** length 111, 32.1% of its response variance represented; |z| ≥ 3 in 774 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.7 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.0 | +1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.9 | +2.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.2 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.4 | -5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.6 | -4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.2 | -5.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.2 | -3.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -4.1 | -3.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.0 | -4.8 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.6 | -2.4 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -2.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.1 — chr3:132,417,502-132,539,032 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RME8, KIAA0678 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins; Armadillo like helical domain containing |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [O75165](https://www.uniprot.org/uniprotkb/O75165) (DnaJ homolog subfamily C member 13):

> Involved in membrane trafficking through early endosomes, such as the early endosome to recycling endosome transport implicated in the recycling of transferrin and the early endosome to late endosome transport implicated in degradation of EGF and EGFR. Involved in the regulation of endosomal membrane tubulation and regulates the dynamics of SNX1 on the endosomal membrane; via association with WASHC2 may link the WASH complex to the retromer SNX-BAR subcomplex.

**Summary**, from NCBI Gene [23317](https://www.ncbi.nlm.nih.gov/gene/23317):

> This gene encodes a member of the Dnaj protein family whose members act as co-chaperones of a partner heat-shock protein by binding to the latter and stimulating ATP hydrolysis. The encoded protein associates with the heat-shock protein Hsc70 and plays a role in clathrin-mediated endocytosis. It may also be involved in post-endocytic transport mechanisms via its associations with other proteins, including the sorting nexin SNX1. Mutations in this gene are associated with Parkinson's disease. …

**Accessions** — [HGNC:30343](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30343) · Entrez [23317](https://www.ncbi.nlm.nih.gov/gene/23317) · UniProt [O75165](https://www.uniprot.org/uniprotkb/O75165) · Ensembl [ENSG00000138246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138246)

## Data

Gene col 6145: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6145); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6145, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6145]; `tensor/DDL_lfc|DDL_z.npy` [6145]; `embed/gene_vectors.npy` [6145]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6145 or target_col == 6145). Every well: [[DNAJC13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
