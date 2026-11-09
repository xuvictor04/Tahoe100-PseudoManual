---
symbol: "NTS"
type: "gene"
col: 5459
ensembl_id: "ENSG00000133636"
name: "neurotensin"
location: "12q21.31"
module: 104
arm: "+"
pooled_cpm: 2.65
n_lines_expressing: 12
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# NTS

*neurotensin* — 12q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 9.09× (z +9.4, q 2e-18, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Medroxyprogesterone acetate (drug)]] 0.5 µM: 3.05× (z +4.7, q 2e-04, up in 2 of 4 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.0135×; ⚠ cell-cycle shift, explains ~83% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.114×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MT1A]] (+0.56, fdr 3e-05), [[SAA1]] (+0.55, fdr 9e-05), [[DNER]] (+0.53, fdr 3e-04); moves opposite to [[ZNF624]] (-0.46, fdr 9e-05), [[SHKBP1]] (-0.46, fdr 1e-04), [[DCTN2]] (-0.46, fdr 1e-04).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[PID1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5459.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **9.09×** | +9.4 | 2e-18 | 2/2 (SHP-77, NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.15×** | +8.6 | 2e-15 | 1/2 (SHP-77) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.85×** | +7.0 | 6e-10 | 2/2 (SHP-77, NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **3.18×** | +4.9 | 1e-04 | 1/4 (LoVo) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **3.05×** | +4.7 | 2e-04 | 2/4 (SHP-77, NCI-H460) | two highest doses | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **3.03×** | +4.7 | 2e-04 | 2/6 (SHP-77, NCI-H460) | all doses, flat | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **3.01×** | +4.7 | 2e-04 | 2/5 (SHP-77, NCI-H460) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **2.99×** | +4.6 | 2e-04 | 3/6 (SHP-77, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.85×** | +4.3 | 0.001 | 3/4 (LoVo, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.43×** | +3.9 | 0.006 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.47×** | +3.8 | 0.007 | 3/5 (NCI-H460, SHP-77, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.90×** | +3.8 | 0.007 | 1/7 (A549) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **5.12×** | +3.6 | 0.012 | 0/2 | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **2.26×** | +3.5 | 0.023 | 3/6 (SHP-77, NCI-H460, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.25×** | +3.4 | 0.023 | 2/5 (SHP-77, NCI-H460) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **2.13×** | +3.2 | 0.048 | 2/6 (SHP-77, NCI-H460) | all doses, flat | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +3.0 | 0.077 | 1/4 (A549) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.0135×; ⚠ cell-cycle shift, explains ~83% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.114×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5459. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 86.7 | 1 | 1 (1 ⚠) | [[Triamcinolone (drug)]] 0.5 µM 9.16× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.0135× (z -22.6) ⚠ cell-cycle shift, explains ~83% of this change |
| [[NCI-H460 (line)]] | wt | 13.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -8.9) |
| [[A-172 (line)]] | wt | 0.466 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.646 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.248 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.714 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.330 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.869 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.272 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.284 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.336 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.330 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.313 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.527 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.284 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.419 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.289 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.256 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.240 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.240 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.245 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.309 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.324 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.289 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.352 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.771 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.759 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.375 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.265 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.553 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.281 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5459), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT1A]] | +0.56 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[SAA1]] | +0.55 | +0.36 / +0.48 | both halves | 9e-05 | pathway: Class A/1 (Rhodopsin-like receptors) |
| [[DNER]] | +0.53 | +0.44 / +0.27 | both halves | 3e-04 |  |
| [[PID1]] | +0.52 | +0.41 / +0.35 | both halves | 1e-04 |  |
| [[JPH2]] | +0.51 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[BCL6]] | +0.50 | +0.44 / +0.38 | both halves | 7e-05 |  |
| [[HS3ST3B1]] | +0.49 | +0.33 / +0.42 | both halves | 1e-04 |  |
| [[CCND3]] | +0.49 | +0.48 / +0.31 | both halves | 2e-04 |  |
| [[IRAK3]] | +0.49 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[TPCN1]] | +0.49 | +0.45 / +0.35 | both halves | 1e-04 |  |
| [[APRT]] | +0.49 | +0.43 / +0.39 | both halves | 6e-05 |  |
| [[ATP1A1]] | +0.48 | +0.51 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF624]] | -0.46 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[SHKBP1]] | -0.46 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[DCTN2]] | -0.46 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[CLIP1]] | -0.43 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[BBOX1-AS1]] | -0.42 | -0.30 / -0.34 | both halves | 2e-04 |  |
| [[ZNF678]] | -0.42 | -0.37 / -0.26 | both halves | 4e-04 |  |
| [[DNAJB2]] | -0.42 | -0.44 / -0.25 | both halves | 4e-04 |  |
| [[TTC7B]] | -0.42 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[SHTN1]] | -0.42 | -0.42 / -0.29 | both halves | 3e-04 |  |
| [[FLII]] | -0.41 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[LARP6]] | -0.41 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[ANXA7]] | -0.40 | -0.41 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PID1]] | C | NTS activity raises PID1's level | lines that do not express NTS (38) vs lines expressing it (12) | 2.37× lower at baseline in the lines without NTS | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, LINC03000, ENSG00000260364; co-absent with the target |
| [[DNER]] | C | NTS activity raises DNER's level | lines that do not express NTS (38) vs lines expressing it (12) | 2.74× lower at baseline in the lines without NTS | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, LINC03000, ENSG00000260364; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.2, 15.6); signed map (17.2, 32.0). **Vector** length 12.7, 2.66% of its response variance represented; |z| ≥ 3 in 126 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +0.6 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.5 | +2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +0.5 | +1.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +0.5 | +3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.4 | +0.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +0.4 | +4.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +0.4 | +4.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +0.4 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -0.7 | -1.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | -0.6 | +2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.5 | +1.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.5 | -0.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.4 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.4 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.4 | +0.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.4 | -1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | neurotensin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.31 — chr12:85,874,295-85,882,992 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Neuropeptides |
| Reactome | 6 pathways, smallest: Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P30990](https://www.uniprot.org/uniprotkb/P30990) (Neurotensin/neuromedin N):

> Neurotensin may play an endocrine or paracrine role in the regulation of fat metabolism. It causes contraction of smooth muscle.

**Summary**, from NCBI Gene [4922](https://www.ncbi.nlm.nih.gov/gene/4922):

> This gene encodes a common precursor for two peptides, neuromedin N and neurotensin. Neurotensin is a secreted tridecapeptide, which is widely distributed throughout the central nervous system, and may function as a neurotransmitter or a neuromodulator. It may be involved in dopamine-associated pathophysiological events, in the maintenance of gut structure and function, and in the regulation of fat metabolism. Neurotensin also exhibits antimicrobial activity against bacteria and fungi. …

**Accessions** — [HGNC:8038](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8038) · Entrez [4922](https://www.ncbi.nlm.nih.gov/gene/4922) · UniProt [P30990](https://www.uniprot.org/uniprotkb/P30990) · Ensembl [ENSG00000133636](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133636)

## Data

Gene col 5459: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5459); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5459, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5459]; `tensor/DDL_lfc|DDL_z.npy` [5459]; `embed/gene_vectors.npy` [5459]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5459 or target_col == 5459). Every well: [[NTS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NTS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
