---
symbol: "CAMLG"
type: "gene"
col: 8972
ensembl_id: "ENSG00000164615"
name: "calcium modulating ligand"
location: "5q31.1"
module: 43
arm: "+"
pooled_cpm: 67.77
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# CAMLG

*calcium modulating ligand* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.82× (z +4.6, q 0.003, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.655× (z -4.5, q 0.004, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HS-578T 0.324×, AsPC-1 0.444×); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.210×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL18]] (+0.87, fdr 7e-06, ⚠ RPL18 in the vector space only through flagged drug-doses), [[RPL31]] (+0.83, fdr 7e-06), [[RPL35A]] (+0.83, fdr 7e-06), [[COMMD6]] (+0.83, fdr 7e-06); moves opposite to [[HNRNPL]] (-0.78, fdr 7e-06), [[HNRNPK]] (-0.75, fdr 7e-06), [[PSME3]] (-0.73, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8972.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.82×** | +4.6 | 0.003 | 44/48 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +4.3 | 0.006 | 41/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +4.0 | 0.012 | 40/47 (SHP-77, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.67×** | +3.9 | 0.012 | 41/48 (BT-474, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +3.9 | 0.012 | 38/48 (HepG2/C3A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +3.7 | 0.019 | 37/48 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +3.5 | 0.042 | 40/48 (NCI-H2030, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8972.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HS-578T 0.324×, AsPC-1 0.444×); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.210×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.655×** | -4.5 | 0.004 | 34/48 (HS-578T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | 0.415× | -3.5 | 0.14 | 39/48 (A-427, SNU-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.439× | -3.3 | 0.21 | 38/49 (A-172, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8972. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 100 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -8.8) |
| [[HS-578T (line)]] | alt | 96.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 55.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 89.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 73.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 83.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 74.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 89.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 67.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 69.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 78.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 70.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 82.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 67.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 94.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 75.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 73.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 69.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8972), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 18 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL18]] ⚠ | +0.87 | +0.73 / +0.88 | both halves | 7e-06 | pathway: Protein localization; ⚠ in the vector space only through flagged drug-doses |
| [[RPL31]] | +0.83 | +0.77 / +0.83 | both halves | 7e-06 | pathway: Protein localization |
| [[RPL35A]] | +0.83 | +0.77 / +0.82 | both halves | 7e-06 | pathway: Protein localization |
| [[COMMD6]] | +0.83 | +0.68 / +0.84 | both halves | 7e-06 |  |
| [[SNHG7]] | +0.83 | +0.63 / +0.88 | both halves | 7e-06 |  |
| [[RPS27]] | +0.83 | +0.74 / +0.84 | both halves | 7e-06 | pathway: Protein localization |
| [[RPL34]] | +0.82 | +0.77 / +0.81 | both halves | 7e-06 | pathway: Protein localization |
| [[SNHG6]] | +0.82 | +0.73 / +0.84 | both halves | 7e-06 |  |
| [[NACA4P]] ⚠ | +0.81 | +0.69 / +0.84 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS14]] | +0.81 | +0.67 / +0.82 | both halves | 7e-06 | pathway: Protein localization |
| [[ATP5MJ]] | +0.81 | +0.65 / +0.81 | both halves | 7e-06 |  |
| [[RPL36]] | +0.81 | +0.67 / +0.83 | both halves | 7e-06 | pathway: Protein localization |
| [[RPL26]] | +0.80 | +0.75 / +0.79 | both halves | 7e-06 | pathway: Protein localization |
| [[RPL17]] | +0.80 | +0.69 / +0.82 | both halves | 7e-06 | pathway: Protein localization |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPL]] | -0.78 | -0.69 / -0.77 | both halves | 7e-06 |  |
| [[HNRNPK]] | -0.75 | -0.70 / -0.68 | both halves | 7e-06 |  |
| [[PSME3]] | -0.73 | -0.63 / -0.79 | both halves | 7e-06 |  |
| [[TUG1]] | -0.72 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[EIF4G2]] | -0.71 | -0.58 / -0.68 | both halves | 8e-06 |  |
| [[SF3B4]] | -0.70 | -0.56 / -0.73 | both halves | 1e-05 |  |
| [[WDR1]] | -0.70 | -0.59 / -0.75 | both halves | 7e-06 |  |
| [[DARS2]] | -0.69 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[NUP188]] | -0.69 | -0.63 / -0.74 | both halves | 7e-06 |  |
| [[YWHAE]] | -0.68 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[U2AF2]] | -0.68 | -0.43 / -0.70 | both halves | 3e-05 |  |
| [[ADAT1]] | -0.68 | -0.66 / -0.57 | both halves | 8e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CAMLG's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers CAMLG's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.801). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-42.6, -26.7); signed map (-25.9, 9.0). **Vector** length 114, 48.0% of its response variance represented; |z| ≥ 3 in 508 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.66 to 55); *Peptide chain elongation* (reactome, mean cos +0.67 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.66 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.2 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.0 | +3.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.6 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +2.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.6 | +1.8 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.4 | -0.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -8.2 | +0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.1 | +0.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.1 | -4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.7 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -2.9 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.6 | -1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | calcium modulating ligand |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:134,738,495-134,752,157 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAML, GET2 |
| Gene groups (HGNC) | Guided entry of tail-anchored proteins complex subunits |
| Reactome | 2 pathways, smallest: Insertion of tail-anchored proteins into the endoplasmic reticulum membrane; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [P49069](https://www.uniprot.org/uniprotkb/P49069) (Guided entry of tail-anchored proteins factor CAMLG):

> Required for the post-translational delivery of tail-anchored (TA) proteins to the endoplasmic reticulum. Together with GET1/WRB, acts as a membrane receptor for soluble GET3/TRC40, which recognizes and selectively binds the transmembrane domain of TA proteins in the cytosol. Required for the stability of GET1. Stimulates calcium signaling in T cells through its involvement in elevation of intracellular calcium. Essential for the survival of peripheral follicular B cells (By similarity).

**Summary**, from NCBI Gene [819](https://www.ncbi.nlm.nih.gov/gene/819):

> The immunosuppressant drug cyclosporin A blocks a calcium-dependent signal from the T-cell receptor (TCR) that normally leads to T-cell activation. When bound to cyclophilin B, cyclosporin A binds and inactivates the key signaling intermediate calcineurin. The protein encoded by this gene functions similarly to cyclosporin A, binding to cyclophilin B and acting downstream of the TCR and upstream of calcineurin by causing an influx of calcium. This integral membrane protein appears to be a new …

**Accessions** — [HGNC:1471](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1471) · Entrez [819](https://www.ncbi.nlm.nih.gov/gene/819) · UniProt [P49069](https://www.uniprot.org/uniprotkb/P49069) · Ensembl [ENSG00000164615](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164615)

## Data

Gene col 8972: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8972); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8972, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8972]; `tensor/DDL_lfc|DDL_z.npy` [8972]; `embed/gene_vectors.npy` [8972]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8972 or target_col == 8972). Every well: [[CAMLG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAMLG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
