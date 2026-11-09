---
symbol: "ARL2"
type: "gene"
col: 13106
ensembl_id: "ENSG00000213465"
name: "ARF like GTPase 2"
location: "11q13.1"
module: 29
arm: "+"
pooled_cpm: 12.52
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# ARL2

*ARF like GTPase 2* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.97× (z +11.2, q 2e-26, up in 36 of 37 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H1573 12.2×, HOP62 6.32×, SNU-423 5.83×, NCI-H460 5.78×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.699× (z -4.1, q 0.022, down in 26 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.159×, BT-474 0.141×); [[Digitoxin (drug)]] 5 µM in 1 line (BT-474 0.0553×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 1 line (BT-474 0.0667×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0832×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NME4]] (+0.63, fdr 1e-05), [[FAM104B]] (+0.60, fdr 2e-05), [[ATP6V0E2]] (+0.60, fdr 1e-05); moves opposite to [[GPN2]] (-0.55, fdr 1e-04), [[ZNF778]] (-0.54, fdr 5e-05), [[ADGRL1-AS1]] (-0.51, fdr 5e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF547]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13106.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H1573 12.2×, HOP62 6.32×, SNU-423 5.83×, NCI-H460 5.78×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.97×** | +11.2 | 2e-26 | 36/37 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.63×** | +10.1 | 2e-21 | 22/23 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.64×** | +7.3 | 6e-11 | 25/29 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.79×** | +4.8 | 3e-04 | 22/39 (A549, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.1 | 0.004 | 23/40 (CFPAC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13106.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.159×, BT-474 0.141×); [[Digitoxin (drug)]] 5 µM in 1 line (BT-474 0.0553×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 1 line (BT-474 0.0667×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0832×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.699×** | -4.1 | 0.022 | 26/47 (MIA PaCa-2, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.681× | -3.1 | 0.36 | 11/46 (SW480, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 0.683× | -3.1 | 0.36 | 19/47 (BT-474, AsPC-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13106. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 12.3 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0553× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.141× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 7.62 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 12.2× (z +10.4) ⚠ toxic; transcription drop | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0832× (z -10.3) |
| [[HOP62 (line)]] | alt | 17.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.32× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 16.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.13× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 6.25 | 0 | 1 | — | [[Roxadustat (drug)]] 5 µM 0.0966× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 7.46 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.78× (z +8.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 8.63 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0759× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 14.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.83× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 8.27 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13106), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 8 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NME4]] | +0.63 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[FAM104B]] | +0.60 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[ATP6V0E2]] | +0.60 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[ATRAID]] | +0.57 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[PYURF]] | +0.57 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[COMMD8]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[CDKN2AIPNL]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[TMEM147]] | +0.54 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[DNPH1]] | +0.54 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[HINT2]] | +0.54 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[THEM6]] | +0.54 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[TMEM106C]] | +0.53 | +0.48 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPN2]] | -0.55 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[ZNF778]] | -0.54 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[ADGRL1-AS1]] | -0.51 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[ZNF547]] | -0.51 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[CDK11A]] | -0.50 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[NOXRED1]] | -0.50 | -0.41 / -0.37 | both halves | 9e-05 |  |
| [[PPP1R26-AS1]] | -0.49 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[UBE2CP5]] | -0.48 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[TMEM92-AS1]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[LINC01772]] | -0.47 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[GMIP]] | -0.45 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[C19orf25]] | -0.45 | -0.45 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF547]] | B | ZNF547 activity lowers ARL2's level | lines that do not express ZNF547 (6) vs lines expressing it (44) | 1.16× higher at baseline in the lines without ZNF547 | 0.083 | ⚠ within organs, on part of the lines; also absent: TRAPPC2B, ZNF548, SPACA6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.436). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-49.2, -12.9); signed map (-22.3, -41.5). **Vector** length 46.9, 7.38% of its response variance represented; |z| ≥ 3 in 596 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +1.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.8 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +11.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | -0.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.1 | +1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.9 | -0.4 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +0.9 | +2.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.4 | -3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.2 | +0.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -0.8 | -0.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -0.8 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,014,160-65,022,184 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARFL2 |
| Gene groups (HGNC) | ARF GTPase family; MicroRNA protein coding host genes |
| Reactome | 10 pathways, smallest: Transport of nucleosides and free purine and pyrimidine bases across the plasma membrane; Post-chaperonin tubulin folding pathway; RAS processing |
| Matched by | ensembl_id |

**Function**, from UniProt [P36404](https://www.uniprot.org/uniprotkb/P36404) (ADP-ribosylation factor-like protein 2):

> Small GTP-binding protein which cycles between an inactive GDP-bound and an active GTP-bound form, and the rate of cycling is regulated by guanine nucleotide exchange factors (GEF) and GTPase-activating proteins (GAP). GTP-binding protein that does not act as an allosteric activator of the cholera toxin catalytic subunit. Regulates formation of new microtubules and centrosome integrity. Prevents the TBCD-induced microtubule destruction. Participates in association with TBCD, in the disassembly …

**Summary**, from NCBI Gene [402](https://www.ncbi.nlm.nih.gov/gene/402):

> This gene encodes a small GTP-binding protein of the RAS superfamily which functions as an ADP-ribosylation factor (ARF). The encoded protein is one of a functionally distinct group of ARF-like genes. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:693](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:693) · Entrez [402](https://www.ncbi.nlm.nih.gov/gene/402) · UniProt [P36404](https://www.uniprot.org/uniprotkb/P36404) · Ensembl [ENSG00000213465](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213465)

## Data

Gene col 13106: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13106); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13106, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13106]; `tensor/DDL_lfc|DDL_z.npy` [13106]; `embed/gene_vectors.npy` [13106]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13106 or target_col == 13106). Every well: [[ARL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
