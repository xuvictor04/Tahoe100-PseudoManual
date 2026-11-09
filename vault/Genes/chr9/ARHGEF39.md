---
symbol: "ARHGEF39"
type: "gene"
col: 5973
ensembl_id: "ENSG00000137135"
name: "Rho guanine nucleotide exchange factor 39"
location: "9p13.3"
module: 22
arm: "+"
pooled_cpm: 3.77
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# ARHGEF39

*Rho guanine nucleotide exchange factor 39* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +9.1, q 5e-17, up in 17 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.446× (z -8.5, q 8e-15, down in 25 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MKI67]] (+0.79, fdr 7e-06), [[CDK1]] (+0.79, fdr 7e-06), [[KIF11]] (+0.78, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RDM1P5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5973.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +9.1 | 5e-17 | 17/33 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.41×** | +8.9 | 1e-16 | 2/3 (PANC-1, HOP62) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **2.06×** | +7.7 | 4e-12 | 11/21 (NCI-H2030, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.86×** | +6.6 | 7e-09 | 11/19 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.41×** | +5.2 | 3e-05 | 18/44 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.40×** | +5.1 | 4e-05 | 13/35 (LOX-IMVI, NCI-H2030, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.62×** | +4.7 | 2e-04 | 2/7 (A498, SW480) | all doses, stronger at high dose | composition shift |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.42×** | +3.7 | 0.014 | 11/44 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.024 | 3/47 (KATO III, LS 180, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.40×** | +3.5 | 0.024 | 4/44 (LS 180, PANC-1, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +3.5 | 0.026 | 2/10 (SW480, HEC-1-A) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.35×** | +3.2 | 0.066 | 4/44 (PANC-1, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5973.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.446×** | -8.5 | 8e-15 | 25/43 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.564×** | -5.7 | 3e-06 | 20/40 (KATO III, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.599×** | -5.4 | 1e-05 | 15/43 (LOX-IMVI, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.659×** | -4.4 | 0.001 | 13/41 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.668×** | -4.3 | 0.002 | 16/46 (HCT15, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.689×** | -3.9 | 0.008 | 12/41 (A-427, LS 180, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.776×** | -3.8 | 0.012 | 10/45 (SW480, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.723×** | -3.4 | 0.043 | 12/36 (LS 180, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.726×** | -3.4 | 0.044 | 13/41 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.733×** | -3.3 | 0.057 | 14/46 (A-427, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.554×** | -3.3 | 0.057 | 9/41 (LoVo, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.808×** | -3.2 | 0.067 | 12/47 (SK-MEL-2, Hs 766T, …) | top dose only |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.799×** | -3.2 | 0.067 | 5/44 (SNU-1, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.62 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5973. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 3.00 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0453× (z -10.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0880× (z -9.0) |
| [[PANC-1 (line)]] | alt | 5.82 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.114× (z -11.0) |
| [[A549 (line)]] | wt | 4.01 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0641× (z -8.8) |
| [[HCT15 (line)]] | alt | 8.23 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0415× (z -9.8) ⚠ cell-cycle shift, explains ~43% of this change |
| [[HT-29 (line)]] | alt | 5.46 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0908× (z -9.3) |
| [[J82 (line)]] | alt | 4.09 | 0 | 1 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0607× (z -10.3) ⚠ toxic |
| [[KATO III (line)]] | alt | 6.98 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0334× (z -12.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[LS 180 (line)]] | wt | 6.63 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0916× (z -9.1) |
| [[A-172 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5973), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKI67]] | +0.79 | +0.80 / +0.78 | both halves | 7e-06 |  |
| [[CDK1]] | +0.79 | +0.79 / +0.77 | both halves | 7e-06 |  |
| [[KIF11]] | +0.78 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[KIF23]] | +0.78 | +0.78 / +0.77 | both halves | 7e-06 |  |
| [[AURKA]] | +0.77 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[NCAPG]] | +0.77 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[TPX2]] | +0.77 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[BIRC5]] | +0.77 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[CCNB2]] | +0.76 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[FAM83D]] | +0.76 | +0.69 / +0.79 | both halves | 7e-06 |  |
| [[CCNA2]] | +0.76 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[KIF2C]] | +0.75 | +0.69 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RDM1P5]] | B | RDM1P5 activity raises ARHGEF39's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.80× lower at baseline in the lines without RDM1P5 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[YBX2]] | B | YBX2 activity raises ARHGEF39's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 1.50× lower at baseline in the lines without YBX2 | 0.055 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.798). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.1, -54.9); signed map (-48.8, -44.2). **Vector** length 64.6, 10.4% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.64 to 60); *DREAM G2/M down* (control, mean cos +0.71 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.58 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.8 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +4.0 | +8.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | +3.8 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +3.5 | +4.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +0.9 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.2 | +3.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.6 | -8.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.5 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -4.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | -2.5 | -3.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.7 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | Rho guanine nucleotide exchange factor 39 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:35,658,875-35,675,866 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14642; previously C9orf100 |
| Gene groups (HGNC) | Dbl family Rho GEFs |
| Reactome | 11 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; Cell death signalling via NRAGE, NRIF and NADE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4T4](https://www.uniprot.org/uniprotkb/Q8N4T4) (Rho guanine nucleotide exchange factor 39):

> Promotes cell proliferation.

**Summary**, from NCBI Gene [84904](https://www.ncbi.nlm.nih.gov/gene/84904):

> Predicted to enable guanyl-nucleotide exchange factor activity. Involved in positive regulation of cell migration. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25909](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25909) · Entrez [84904](https://www.ncbi.nlm.nih.gov/gene/84904) · UniProt [Q8N4T4](https://www.uniprot.org/uniprotkb/Q8N4T4) · Ensembl [ENSG00000137135](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137135)

## Data

Gene col 5973: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5973); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5973, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5973]; `tensor/DDL_lfc|DDL_z.npy` [5973]; `embed/gene_vectors.npy` [5973]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5973 or target_col == 5973). Every well: [[ARHGEF39 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF39.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
