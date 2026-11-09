---
symbol: "SEC23IP"
type: "gene"
col: 2866
ensembl_id: "ENSG00000107651"
name: "SEC23 interacting protein"
location: "10q26.11-q26.12"
module: 41
arm: "+"
pooled_cpm: 87.62
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# SEC23IP

*SEC23 interacting protein* — 10q26.11-q26.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.62× (z +9.5, q 1e-18, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.656× (z -8.4, q 3e-14, down in 34 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.720× (z -6.3, q 4e-08, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COG3]] (+0.80, fdr 7e-06), [[GOSR2]] (+0.74, fdr 7e-06), [[GOSR1]] (+0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[SPTY2D1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2866.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +9.5 | 1e-18 | 41/48 (SNU-1, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +9.3 | 3e-18 | 36/48 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +8.9 | 1e-16 | 35/48 (SNU-423, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.24×** | +8.3 | 1e-14 | 36/49 (A498, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.77×** | +5.9 | 4e-07 | 31/48 (A-172, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +5.4 | 6e-06 | 29/48 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.25×** | +4.4 | 7e-04 | 25/48 (RKO, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +4.4 | 7e-04 | 26/48 (NCI-H2347, MIA PaCa-2, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.049 | 15/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.18× | +3.2 | 0.076 | 16/48 (PANC-1, SNU-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.076 | 12/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2866.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.656×** | -8.4 | 3e-14 | 34/49 (CHP-212, SW 900, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.697×** | -6.9 | 1e-09 | 32/44 (hTERT-HPNE, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.696×** | -6.7 | 5e-09 | 29/45 (NCI-H2347, SW 900, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.720×** | -6.3 | 4e-08 | 29/48 (HCT15, NCI-H2030, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.813×** | -5.4 | 7e-06 | 31/49 (LoVo, SNU-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.832×** | -3.7 | 0.023 | 19/48 (C32, RKO, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.854× | -3.2 | 0.11 | 17/48 (LoVo, HCT15, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.854× | -3.2 | 0.11 | 19/48 (AsPC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2866. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 101 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.73× (z +9.3) | [[Belinostat (drug)]] 5 µM 0.579× (z -9.2) ⚠ cell-cycle shift, explains ~9% of this change |
| [[NCI-H460 (line)]] | wt | 95.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 80.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 61.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 49.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 130 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 136 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -12.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0434× (z -20.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 82.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -8.7) ⚠ cell-cycle shift, explains ~17% of this change |
| [[hTERT-HPNE (line)]] | wt | 95.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -10.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 105 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 73.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.72× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 76.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.409× (z -10.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 86.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -10.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 93.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -10.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 82.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +11.6) | — |
| [[A-427 (line)]] | wt | 65.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 112 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 80.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 102 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 91.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 83.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 74.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 96.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 67.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 84.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2866), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG3]] | +0.80 | +0.73 / +0.78 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[GOSR2]] | +0.74 | +0.74 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 677 |
| [[GOSR1]] | +0.71 | +0.71 / +0.64 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SLC30A5]] | +0.71 | +0.67 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[SPTY2D1]] | +0.69 | +0.75 / +0.58 | both halves | 7e-06 |  |
| [[PGM3]] | +0.69 | +0.69 / +0.60 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[KDELR2]] | +0.68 | +0.65 / +0.71 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PMM2]] | +0.67 | +0.63 / +0.60 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[GOLGA5]] | +0.67 | +0.72 / +0.54 | both halves | 1e-05 | STRING 475 |
| [[SCFD1]] | +0.67 | +0.65 / +0.66 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 792 |
| [[LYSMD3]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[OSBP]] | +0.66 | +0.71 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPTY2D1]] | C | SEC23IP's natural level weakens SPTY2D1's drug response | SEC23IP's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.67, reverse -0.04; direction clear | 0.027 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.647). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (12.5, -36.8); signed map (-52.5, 12.9). **Vector** length 103, 28.0% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.6 | +9.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | +9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | +2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | +8.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.4 | +3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.8 | +3.4 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.1 | +1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.0 | +4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | +1.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -6.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | +0.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.2 | -1.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | SEC23 interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.11-q26.12 — chr10:119,892,707-119,944,657 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p125, iPLA1beta, iPLA1β, p125A |
| Gene groups (HGNC) | Sterile alpha motif domain containing |
| Reactome | 6 pathways, smallest: COPII-mediated vesicle transport; ER to Golgi Anterograde Transport; Transport to the Golgi and subsequent modification |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6Y8](https://www.uniprot.org/uniprotkb/Q9Y6Y8) (SEC23-interacting protein):

> Plays a role in the organization of endoplasmic reticulum exit sites. Specifically binds to phosphatidylinositol 3-phosphate (PI(3)P), phosphatidylinositol 4-phosphate (PI(4)P) and phosphatidylinositol 5-phosphate (PI(5)P).

**Summary**, from NCBI Gene [11196](https://www.ncbi.nlm.nih.gov/gene/11196):

> This gene encodes a member of the phosphatidic acid preferring-phospholipase A1 family. The encoded protein is localized to endoplasmic reticulum exit sites and plays a critical role in ER-Golgi transport as part of the multimeric coat protein II complex. An orthologous gene in frogs is required for normal neural crest cell development, suggesting that this gene may play a role in Waardenburg syndrome neural crest defects. Alternatively spliced transcript variants have been observed for this …

**Accessions** — [HGNC:17018](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17018) · Entrez [11196](https://www.ncbi.nlm.nih.gov/gene/11196) · UniProt [Q9Y6Y8](https://www.uniprot.org/uniprotkb/Q9Y6Y8) · Ensembl [ENSG00000107651](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107651)

## Data

Gene col 2866: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2866); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2866, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2866]; `tensor/DDL_lfc|DDL_z.npy` [2866]; `embed/gene_vectors.npy` [2866]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2866 or target_col == 2866). Every well: [[SEC23IP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC23IP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
