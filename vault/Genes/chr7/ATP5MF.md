---
symbol: "ATP5MF"
type: "gene"
col: 14276
ensembl_id: "ENSG00000241468"
name: "ATP synthase membrane subunit f"
location: "7q22.1"
module: 48
arm: "+"
pooled_cpm: 38.11
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# ATP5MF

*ATP synthase membrane subunit f* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.78× (z +9.1, q 3e-17, up in 45 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 8.70×, NCI-H1792 9.92×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[GSK1059615 (drug)]] 5 µM: 0.273× (z -3.9, q 0.053, down in 42 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.129×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (Panc 03.27 0.237×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 25 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UQCR10]] (+0.79, fdr 7e-06, ⚠ UQCR10 in the vector space only through flagged drug-doses), [[ROMO1]] (+0.76, fdr 7e-06), [[UQCRQ]] (+0.75, fdr 7e-06, ⚠ UQCRQ in the vector space only through flagged drug-doses), [[UQCR11]] (+0.70, fdr 1e-05), [[NDUFC2]] (+0.68, fdr 7e-06); moves opposite to [[HAPSTR1]] (-0.51, fdr 3e-04), [[EIF2S3]] (-0.48, fdr 7e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14276.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 8.70×, NCI-H1792 9.92×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **4.78×** | +9.1 | 3e-17 | 45/45 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **3.37×** | +7.5 | 2e-11 | 36/38 (SNU-423, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.44×** | +5.3 | 2e-05 | 35/43 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **2.10×** | +4.8 | 2e-04 | 41/47 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +4.7 | 2e-04 | 44/45 (CFPAC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14276.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.129×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (Panc 03.27 0.237×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **0.273×** | -3.9 | 0.053 | 42/47 (LoVo, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.318× | -3.5 | 0.16 | 39/48 (BT-474, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.349× | -3.2 | 0.24 | 31/48 (LoVo, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.688× | -3.1 | 0.24 | 24/48 (C-33 A, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.593× | -3.1 | 0.24 | 32/48 (J82, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.65 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14276. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 53.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 30.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.70× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H1792 (line)]] | alt | 20.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.92× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[Panc 03.27 (line)]] | alt | 37.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.237× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 56.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 44.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14276), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 25 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCR10]] ⚠ | +0.79 | +0.68 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 909; ⚠ in the vector space only through flagged drug-doses |
| [[ROMO1]] | +0.76 | +0.61 / +0.83 | both halves | 7e-06 |  |
| [[UQCRQ]] ⚠ | +0.75 | +0.65 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 896; ⚠ in the vector space only through flagged drug-doses |
| [[UQCR11]] | +0.70 | +0.56 / +0.78 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 917 |
| [[NDUFC2]] | +0.68 | +0.60 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 672 |
| [[MICOS10]] | +0.68 | +0.59 / +0.76 | both halves | 7e-06 | pathway: Cristae formation; STRING 757 |
| [[CHCHD1]] | +0.67 | +0.36 / +0.79 | both halves | 9e-05 |  |
| [[NDUFA13]] ⚠ | +0.67 | +0.58 / +0.76 | both halves | 8e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 869; ⚠ in the vector space only through flagged drug-doses |
| [[NDUFB1]] | +0.66 | +0.47 / +0.75 | both halves | 2e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 622 |
| [[NDUFB11]] ⚠ | +0.66 | +0.50 / +0.71 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 692; ⚠ in the vector space only through flagged drug-doses |
| [[GADD45GIP1]] | +0.65 | +0.41 / +0.81 | both halves | 4e-05 |  |
| [[C4orf48]] | +0.65 | +0.42 / +0.72 | both halves | 4e-05 |  |
| [[COX6B1]] | +0.65 | +0.47 / +0.73 | both halves | 2e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 808 |
| [[EMC6]] | +0.64 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[MIF]] | +0.64 | +0.43 / +0.73 | both halves | 3e-05 |  |
| [[NDUFA1]] | +0.63 | +0.45 / +0.69 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 803 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAPSTR1]] | -0.51 | -0.27 / -0.60 | both halves | 3e-04 |  |
| [[EIF2S3]] | -0.48 | -0.37 / -0.54 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.667). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-47.5, -21.7); signed map (-35.7, 10.0). **Vector** length 47.7, 14.6% of its response variance represented; |z| ≥ 3 in 464 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Respiratory electron transport* (reactome, mean cos +0.59 to 24); *Complex IV assembly* (reactome, mean cos +0.55 to 11); *Cytoprotection by HMOX1* (reactome, mean cos +0.56 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.4 | +2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | -0.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.9 | +2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.9 | +2.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +0.9 | -0.6 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -3.2 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -3.2 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -2.9 | +9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | +0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.2 | +1.7 |

## What is on record

|  |  |
|---|---|
| Name | ATP synthase membrane subunit f |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:99,448,475-99,466,186 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATP5JL; previously ATP5J2 |
| Gene groups (HGNC) | Mitochondrial complex V: ATP synthase subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 5 pathways, smallest: Formation of ATP by chemiosmotic coupling; Cristae formation; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P56134](https://www.uniprot.org/uniprotkb/P56134) (ATP synthase F(0) complex subunit f, mitochondrial):

> Subunit f, of the mitochondrial membrane ATP synthase complex (F(1)F(0) ATP synthase or Complex V) that produces ATP from ADP in the presence of a proton gradient across the membrane which is generated by electron transport complexes of the respiratory chain. ATP synthase complex consist of a soluble F(1) head domain - the catalytic core - and a membrane F(1) domain - the membrane proton channel. These two domains are linked by a central stalk rotating inside the F(1) region and a stationary …

**Summary**, from NCBI Gene [9551](https://www.ncbi.nlm.nih.gov/gene/9551):

> Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. It is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, which comprises the proton channel. The catalytic portion of mitochondrial ATP synthase consists of five different subunits (alpha, beta, gamma, delta, and epsilon) assembled with a stoichiometry of 3 alpha, 3 …

**Accessions** — [HGNC:848](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:848) · Entrez [9551](https://www.ncbi.nlm.nih.gov/gene/9551) · UniProt [P56134](https://www.uniprot.org/uniprotkb/P56134) · Ensembl [ENSG00000241468](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241468)

## Data

Gene col 14276: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14276); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14276, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14276]; `tensor/DDL_lfc|DDL_z.npy` [14276]; `embed/gene_vectors.npy` [14276]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14276 or target_col == 14276). Every well: [[ATP5MF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP5MF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
