---
symbol: "LAMTOR2"
type: "gene"
col: 3809
ensembl_id: "ENSG00000116586"
name: "late endosomal/lysosomal adaptor, MAPK and MTOR activator 2"
location: "1q22"
module: 48
arm: "+"
pooled_cpm: 13.26
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 2
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# LAMTOR2

*late endosomal/lysosomal adaptor, MAPK and MTOR activator 2* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.93× (z +9.1, q 6e-17, up in 34 of 35 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.46× (z +4.0, q 0.007, up in 26 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 6.75×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.508× (z -6.9, q 4e-09, down in 35 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H2030 0.247×, HT-29 0.207×, RKO 0.167×, LOX-IMVI 0.135×, …).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPM3]] (+0.76, fdr 7e-06), [[NDUFA2]] (+0.76, fdr 1e-05), [[PCSK1N]] (+0.74, fdr 8e-06); moves opposite to [[SFPQ]] (-0.67, fdr 2e-05), [[SRSF6]] (-0.64, fdr 1e-05), [[HNRNPA2B1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TRAPPC1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3809.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 6.75×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.93×** | +9.1 | 6e-17 | 34/35 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.46×** | +8.7 | 1e-15 | 24/25 (A-172, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.31×** | +5.6 | 3e-06 | 28/31 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.94×** | +4.8 | 2e-04 | 32/41 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +4.5 | 8e-04 | 28/39 (SW480, A498, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.0 | 0.007 | 26/45 (A-172, A549, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.56×** | +3.3 | 0.090 | 21/47 (SW 900, HEC-1-A, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3809.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H2030 0.247×, HT-29 0.207×, RKO 0.167×, LOX-IMVI 0.135×, …).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.508×** | -6.9 | 4e-09 | 35/45 (NCI-H2030, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.473×** | -5.4 | 2e-05 | 31/45 (NCI-H2030, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3809. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.75× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -9.2) |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 6.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 26.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -11.2) |
| [[RKO (line)]] | wt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -10.5) |
| [[A-172 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3809), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 10 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPM3]] | +0.76 | +0.69 / +0.75 | both halves | 7e-06 | STRING 453 |
| [[NDUFA2]] | +0.76 | +0.49 / +0.77 | both halves | 1e-05 |  |
| [[PCSK1N]] | +0.74 | +0.58 / +0.73 | both halves | 8e-06 |  |
| [[MICOS13]] | +0.74 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[COX7C]] | +0.73 | +0.69 / +0.67 | both halves | 7e-06 | pathway: TP53 Regulates Metabolic Genes |
| [[COX14]] | +0.73 | +0.53 / +0.76 | both halves | 1e-05 | STRING 469 |
| [[TMEM256]] | +0.73 | +0.59 / +0.79 | both halves | 7e-06 |  |
| [[ELOB]] | +0.73 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[ALKBH7]] | +0.73 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[C4orf48]] | +0.73 | +0.55 / +0.80 | both halves | 1e-05 |  |
| [[RABAC1]] | +0.73 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[UQCR11]] | +0.72 | +0.61 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFPQ]] | -0.67 | -0.46 / -0.70 | both halves | 2e-05 |  |
| [[SRSF6]] | -0.64 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[HNRNPA2B1]] | -0.62 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[THOC6]] | -0.61 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[SRSF1]] | -0.61 | -0.37 / -0.67 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRAPPC1]] | C | TRAPPC1's natural level strengthens LAMTOR2's drug response | TRAPPC1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.23; direction not clear | 0.063 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.800). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-45.8, -20.3); signed map (-33.4, 9.4). **Vector** length 47.4, 9.12% of its response variance represented; |z| ≥ 3 in 524 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.59 to 31); *Respiratory electron transport* (reactome, mean cos +0.59 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.60 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +1.6 | +3.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.4 | +1.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.4 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.2 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +0.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.1 | +0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.1 | +0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.1 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -0.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -2.5 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -2.2 | +8.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -0.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.0 | -2.5 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -0.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | late endosomal/lysosomal adaptor, MAPK and MTOR activator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:156,054,782-156,058,506 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MAPBPIP, MAPKSP1AP, p14, ENDAP, Ragulator2; previously ROBLD3 |
| Gene groups (HGNC) | Ragulator complex |
| Reactome | 21 pathways, smallest: mTORC1-mediated signalling; Energy dependent regulation of mTOR by LKB1-AMPK; MAP2K and MAPK activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2Q5](https://www.uniprot.org/uniprotkb/Q9Y2Q5) (Ragulator complex protein LAMTOR2):

> As part of the Ragulator complex it is involved in amino acid sensing and activation of mTORC1, a signaling complex promoting cell growth in response to growth factors, energy levels, and amino acids. Activated by amino acids through a mechanism involving the lysosomal V-ATPase, the Ragulator plays a dual role for the small GTPases Rag (RagA/RRAGA, RagB/RRAGB, RagC/RRAGC and/or RagD/RRAGD): it (1) acts as a guanine nucleotide exchange factor (GEF), activating the small GTPases Rag and (2) …

**Summary**, from NCBI Gene [28956](https://www.ncbi.nlm.nih.gov/gene/28956):

> The product of this gene is highly conserved with a mouse protein associated with the cytoplasmic face of late endosomes and lysosomes. The mouse protein interacts with MAPK scaffold protein 1, a component of the mitogen-activated protein kinase pathway. In humans, a mutation in this gene has been associated with a primary immunodeficiency syndrome, and suggests a role for this protein in endosomal biogenesis. Multiple transcript variants encoding different isoforms have been found for this …

**Accessions** — [HGNC:29796](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29796) · Entrez [28956](https://www.ncbi.nlm.nih.gov/gene/28956) · UniProt [Q9Y2Q5](https://www.uniprot.org/uniprotkb/Q9Y2Q5) · Ensembl [ENSG00000116586](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116586)

## Data

Gene col 3809: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3809); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3809, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3809]; `tensor/DDL_lfc|DDL_z.npy` [3809]; `embed/gene_vectors.npy` [3809]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3809 or target_col == 3809). Every well: [[LAMTOR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMTOR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
