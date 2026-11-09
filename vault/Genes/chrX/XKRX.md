---
symbol: "XKRX"
type: "gene"
col: 11291
ensembl_id: "ENSG00000182489"
name: "XK related X-linked"
location: "Xq22.1"
module: 8
arm: "+"
pooled_cpm: 2.03
n_lines_expressing: 41
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# XKRX

*XK related X-linked* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.35× (z +11.6, q 3e-28, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.52× (z +4.3, q 0.003, up in 10 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.530× (z -4.5, q 0.003, down in 15 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H460 0.117×, H4 0.0739×, NCI-H2030 0.0773×, LS 180 0.173×; ⚠ cell-cycle shift, explains ~78% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (H4 0.0317×); [[Belinostat (drug)]] 5 µM in 1 line (H4 0.0426×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK31]] (+0.52, fdr 4e-05), [[LAMB4]] (+0.51, fdr 2e-05), [[FXYD2]] (+0.49, fdr 4e-05); moves opposite to [[CEP250]] (-0.40, fdr 2e-04), [[UBE2I]] (-0.36, fdr 1e-04), [[SLC25A11]] (-0.35, fdr 2e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TCN1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PTPN22]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11291.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.35×** | +11.6 | 3e-28 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.77×** | +7.3 | 9e-11 | 1/10 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.96×** | +7.2 | 1e-10 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +4.3 | 0.003 | 10/30 (SW480, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +3.9 | 0.012 | 5/19 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.70×** | +3.6 | 0.024 | 0/12 | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.69×** | +3.6 | 0.024 | 6/22 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.030 | 3/19 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.2 | 0.074 | 0/12 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11291.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H460 0.117×, H4 0.0739×, NCI-H2030 0.0773×, LS 180 0.173×; ⚠ cell-cycle shift, explains ~78% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (H4 0.0317×); [[Belinostat (drug)]] 5 µM in 1 line (H4 0.0426×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.530×** | -4.5 | 0.003 | 15/27 (H4, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.660×** | -4.3 | 0.004 | 14/21 (NCI-H460, H4, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.556×** | -4.2 | 0.004 | 13/33 (A549, LS 180, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.375×** | -3.7 | 0.030 | 12/23 (H4, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11291. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 18.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0739× (z -12.6) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0317× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 6.13 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -13.5) ⚠ cell-cycle shift, explains ~78% of this change |
| [[LS 180 (line)]] | wt | 5.96 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -9.5) ⚠ cell-cycle shift, explains ~78% of this change |
| [[NCI-H2030 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0773× (z -12.5) ⚠ cell-cycle shift, explains ~78% of this change |
| [[A-172 (line)]] | wt | 0.379 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.828 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.452 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.636 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.319 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.596 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.808 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.516 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.606 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.533 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.562 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.361 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.531 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.247 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.891 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.983 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.531 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11291), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK31]] | +0.52 | +0.40 / +0.47 | both halves | 4e-05 |  |
| [[LAMB4]] | +0.51 | +0.46 / +0.46 | both halves | 2e-05 |  |
| [[FXYD2]] | +0.49 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[CCDC162P]] | +0.49 | +0.39 / +0.57 | both halves | 6e-05 |  |
| [[TARID]] | +0.48 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[MYO1F]] | +0.48 | +0.32 / +0.53 | both halves | 2e-04 |  |
| [[PON3]] | +0.47 | +0.41 / +0.40 | both halves | 5e-05 |  |
| [[HORMAD1]] | +0.47 | +0.46 / +0.31 | both halves | 2e-04 |  |
| [[LINC01290]] | +0.47 | +0.31 / +0.55 | both halves | 2e-04 |  |
| [[ENPEP]] | +0.46 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[DSCAML1]] | +0.46 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[SPX]] | +0.45 | +0.46 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP250]] | -0.40 | -0.30 / -0.34 | both halves | 2e-04 |  |
| [[UBE2I]] | -0.36 | -0.33 / -0.33 | both halves | 1e-04 |  |
| [[SLC25A11]] | -0.35 | -0.32 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCN1]] | B | TCN1 activity raises XKRX's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 1.42× lower at baseline in the lines without TCN1 | 0.044 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[SPOCK2]] | B | SPOCK2 activity raises XKRX's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.57× lower at baseline in the lines without SPOCK2 | 0.073 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPN22]] | B | XKRX activity raises PTPN22's level | lines that do not express XKRX (9) vs lines expressing it (41) | 1.62× lower at baseline in the lines without XKRX | 0.094 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.201). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.8, 43.1); signed map (47.4, 42.7). **Vector** length 40.0, 5.90% of its response variance represented; |z| ≥ 3 in 777 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.6 | +3.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +1.2 |
| fall | [[Radotinib (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -0.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +0.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | XK related X-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:100,913,445-100,929,433 (-) |
| Ensembl biotype | protein_coding |
| Also known as | XPLAC, XKR2 |
| Gene groups (HGNC) | XK related family |
| Matched by | ensembl_id |

UniProt [Q6PP77](https://www.uniprot.org/uniprotkb/Q6PP77) carries no function annotation.

**Summary**, from NCBI Gene [402415](https://www.ncbi.nlm.nih.gov/gene/402415):

> This gene encodes a protein that is related to a component of the XK/Kell complex of the Kell blood group system. The encoded protein includes several transmembrane domains, is known to be exposed to the cell surface, and may function as a membrane transporter. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:29845](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29845) · Entrez [402415](https://www.ncbi.nlm.nih.gov/gene/402415) · UniProt [Q6PP77](https://www.uniprot.org/uniprotkb/Q6PP77) · Ensembl [ENSG00000182489](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182489)

## Data

Gene col 11291: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11291); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11291, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11291]; `tensor/DDL_lfc|DDL_z.npy` [11291]; `embed/gene_vectors.npy` [11291]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11291 or target_col == 11291). Every well: [[XKRX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XKRX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
