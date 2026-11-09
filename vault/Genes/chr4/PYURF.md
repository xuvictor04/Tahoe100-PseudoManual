---
symbol: "PYURF"
type: "gene"
col: 6977
ensembl_id: "ENSG00000145337"
name: "PIGY upstream open reading frame"
location: "4q22.1"
module: 29
arm: "+"
pooled_cpm: 21.76
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# PYURF

*PIGY upstream open reading frame* — 4q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.04× (z +11.7, q 8e-29, up in 39 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.54× (z +4.6, q 5e-04, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[GSK1059615 (drug)]] 5 µM: 0.499× (z -3.8, q 0.073, down in 25 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Saquinavir (drug)]] 5 µM in 1 line (SHP-77 0.271×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.170×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAIP1]] (+0.62, fdr 7e-06), [[MINPP1]] (+0.60, fdr 1e-05), [[COMMD8]] (+0.59, fdr 2e-05); moves opposite to [[ADGRL1-AS1]] (-0.61, fdr 1e-05), [[MFSD11]] (-0.56, fdr 1e-05), [[SPRED3]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[OBSCN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6977.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.04×** | +11.7 | 8e-29 | 39/42 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.71×** | +10.1 | 2e-21 | 30/34 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +7.7 | 3e-12 | 40/46 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.76×** | +5.9 | 4e-07 | 30/45 (HOP62, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.97×** | +5.5 | 4e-06 | 27/39 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +4.6 | 5e-04 | 29/48 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.51×** | +4.2 | 0.002 | 26/47 (COLO 205, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.46×** | +4.0 | 0.004 | 27/48 (HOP62, HEC-1-A, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.68×** | +3.9 | 0.006 | 26/47 (HOP62, C-33 A, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.030 | 20/48 (SNU-423, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **1.35×** | +3.2 | 0.081 | 18/46 (H4, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6977.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Saquinavir (drug)]] 5 µM in 1 line (SHP-77 0.271×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.170×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **0.499×** | -3.8 | 0.073 | 25/46 (RPMI-7951, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.743× | -3.0 | 0.74 | 17/47 (RKO, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6977. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 20.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.07× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[C32 (line)]] | wt | 25.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HepG2_C3A (line)]] | wt | 23.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.170× (z -8.8) ⚠ toxic |
| [[HOP62 (line)]] | alt | 14.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.50× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LoVo (line)]] | wt | 21.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 17.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.60× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[PANC-1 (line)]] | alt | 16.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SHP-77 (line)]] | alt | 15.0 | 0 | 1 | — | [[Saquinavir (drug)]] 5 µM 0.271× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 27.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6977), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAIP1]] | +0.62 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[MINPP1]] | +0.60 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[COMMD8]] | +0.59 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[DNAJC19]] | +0.58 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[HINT3]] | +0.58 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[MANEA]] | +0.58 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[TMEM126B]] | +0.57 | +0.44 / +0.72 | both halves | 3e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[ARL2]] | +0.57 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[COX11]] | +0.57 | +0.58 / +0.54 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[RAB14]] | +0.57 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[SRI]] | +0.57 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[MRPL40]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRL1-AS1]] | -0.61 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[MFSD11]] | -0.56 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[SPRED3]] | -0.56 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[PPP1R13L]] | -0.55 | -0.62 / -0.46 | both halves | 2e-05 |  |
| [[DMPK]] | -0.55 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[GPATCH2L]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[TTLL3]] | -0.52 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[TRIOBP]] | -0.52 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[PROSER3]] | -0.51 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[SPAG5-AS1]] | -0.51 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[SLC9A5]] | -0.51 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[CYTH2]] | -0.51 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OBSCN]] | B | OBSCN activity lowers PYURF's level | lines that do not express OBSCN (9) vs lines expressing it (41) | 1.24× higher at baseline in the lines without OBSCN | 0.035 | ⚠ within organs, on part of the lines; also absent: MAP3K21, C1orf115, CAMK1D; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.514). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-19.8, -1.7); signed map (-19.5, -40.0). **Vector** length 62.7, 12.7% of its response variance represented; |z| ≥ 3 in 648 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.2 | +3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.8 | +4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.2 | -0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.9 | +1.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.7 | +1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -1.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -0.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.2 | -1.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.9 | -1.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | PIGY upstream open reading frame |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.1 — chr4:88,520,998-88,523,776 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PreY |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96I23](https://www.uniprot.org/uniprotkb/Q96I23) (Protein preY, mitochondrial):

> In mitochondria, S-adenosylmethionine-dependent methyltransferase chaperone that supports both coenzyme Q biosynthesis, by stabilizing its components, such as COQ5, and NADH:ubiquinone oxidoreductase complex (complex I, MT-ND1) assembly, by stabilizing complex I assembly factors, such as NDUFAF5.

**Summary**, from NCBI Gene [100996939](https://www.ncbi.nlm.nih.gov/gene/100996939):

> The product of this gene, which is well-conserved, is encoded by the same bicistronic transcript that encodes phosphatidylinositol glycan anchor biosynthesis, class Y, but the two proteins are unrelated. This gene represents the protein encoded by the upstream open reading frame, while the protein encoded by the downstream open reading frame is represented by GeneID:84992. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:44317](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44317) · Entrez [100996939](https://www.ncbi.nlm.nih.gov/gene/100996939) · UniProt [Q96I23](https://www.uniprot.org/uniprotkb/Q96I23) · Ensembl [ENSG00000145337](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145337)

## Data

Gene col 6977: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6977); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6977, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6977]; `tensor/DDL_lfc|DDL_z.npy` [6977]; `embed/gene_vectors.npy` [6977]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6977 or target_col == 6977). Every well: [[PYURF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PYURF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
