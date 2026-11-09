---
symbol: "PRSS53"
type: "gene"
col: 7475
ensembl_id: "ENSG00000151006"
name: "serine protease 53"
location: "16p11.2"
module: 103
arm: "+"
pooled_cpm: 5.41
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 12
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# PRSS53

*serine protease 53* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Bosentan (hydrate) (drug)]] 5 µM: 1.62× (z +4.0, q 0.030, up in 15 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.298× (z -10.0, q 6e-21, down in 36 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3D21]] (+0.72, fdr 7e-06), [[PPFIA4]] (+0.65, fdr 7e-06), [[EOLA1]] (+0.62, fdr 7e-06); moves opposite to [[ZMYM4]] (-0.58, fdr 1e-05), [[ZNF644]] (-0.56, fdr 1e-05), [[LYRM2]] (-0.54, fdr 1e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AMIGO2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7475.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.62×** | +4.0 | 0.030 | 15/39 (RPMI-7951, NCI-H2347, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7475.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.298×** | -10.0 | 6e-21 | 36/45 (SW 900, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.441×** | -10.0 | 6e-21 | 35/43 (MIA PaCa-2, HOP62, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.419×** | -7.2 | 1e-10 | 27/35 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.488×** | -6.2 | 1e-07 | 23/45 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.539×** | -5.3 | 1e-05 | 24/39 (A-172, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.667×** | -4.9 | 9e-05 | 19/46 (LOX-IMVI, H4, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.367×** | -4.5 | 5e-04 | 19/42 (MIA PaCa-2, HepG2/C3A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.597×** | -4.4 | 7e-04 | 19/46 (SK-MEL-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.630×** | -3.7 | 0.012 | 13/43 (C32, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.640×** | -3.7 | 0.013 | 15/43 (C32, SNU-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.695×** | -3.1 | 0.096 | 17/39 (SNU-423, LOX-IMVI, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.697×** | -3.1 | 0.097 | 6/47 (A-172, SW 1088, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7475. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 13.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -12.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0696× (z -12.5) |
| [[HOP62 (line)]] | alt | 8.62 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -13.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 17.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -13.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.175× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 4.70 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -10.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0853× (z -9.6) |
| [[HS-578T (line)]] | alt | 7.82 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0795× (z -13.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0846× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0906× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 8.02 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0932× (z -9.1) |
| [[SNU-423 (line)]] | alt | 6.43 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0753× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 7.96 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0530× (z -9.2) ⚠ cell-cycle shift, explains ~99% of this change |
| [[NCI-H2030 (line)]] | alt | 3.86 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0654× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 4.99 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0784× (z -9.5) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 2.97 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0909× (z -8.8) |
| [[SW 900 (line)]] | alt | 4.88 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0407× (z -9.7) |
| [[A-427 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7475), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3D21]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[PPFIA4]] | +0.65 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[EOLA1]] | +0.62 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[ARFGAP1]] | +0.62 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[PKD1]] | +0.62 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[CRYBB2P1-1]] | +0.62 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[CRYBB2P1]] | +0.60 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[LINC01128]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[MAPK7]] | +0.58 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[STK32C]] | +0.58 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[LONP1]] | +0.58 | +0.61 / +0.56 | both halves | 1e-05 | same gene group |
| [[AJM1]] | +0.58 | +0.58 / +0.60 | both halves | 8e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM4]] | -0.58 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[ZNF644]] | -0.56 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[LYRM2]] | -0.54 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[ERBIN]] | -0.54 | -0.43 / -0.51 | both halves | 4e-05 |  |
| [[ATXN7L1]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[AASDHPPT]] | -0.53 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[SLX4IP]] | -0.52 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[MRPS33]] | -0.52 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[COMMD8]] | -0.52 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[LARP7]] | -0.51 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[PPP1R9A]] | -0.51 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[ARHGAP42]] | -0.50 | -0.51 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AMIGO2]] | B | AMIGO2 activity lowers PRSS53's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 1.45× higher at baseline in the lines without AMIGO2 | 0.037 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[STARD9]] | B | STARD9 activity raises PRSS53's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 2.01× lower at baseline in the lines without STARD9 | 0.057 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.581). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.8, -22.6); signed map (-40.0, 25.6). **Vector** length 70.9, 11.4% of its response variance represented; |z| ≥ 3 in 1,076 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.1 | +2.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +1.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | +2.0 | +1.1 |
|  | [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.7 | +2.5 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +1.7 | +1.8 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.6 | +4.0 |
|  | [[Roxadustat (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.5 | +0.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.5 | +1.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.7 | -10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.7 | -10.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.3 | -4.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.2 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.7 | -5.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.4 | -3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -3.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.1 | -2.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.0 | -1.3 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | serine protease 53 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:31,083,437-31,089,628 (-) |
| Ensembl biotype | protein_coding |
| Also known as | POL3S |
| Gene groups (HGNC) | Serine proteases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2L4Q9](https://www.uniprot.org/uniprotkb/Q2L4Q9) (Serine protease 53):

> In vitro can degrade the fibrinogen alpha chain of as well as pro-urokinase-type plasminogen activator.

**Summary**, from NCBI Gene [339105](https://www.ncbi.nlm.nih.gov/gene/339105):

> Predicted to enable serine-type endopeptidase activity. Predicted to be involved in proteolysis. Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:34407](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34407) · Entrez [339105](https://www.ncbi.nlm.nih.gov/gene/339105) · UniProt [Q2L4Q9](https://www.uniprot.org/uniprotkb/Q2L4Q9) · Ensembl [ENSG00000151006](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151006)

## Data

Gene col 7475: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7475); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7475, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7475]; `tensor/DDL_lfc|DDL_z.npy` [7475]; `embed/gene_vectors.npy` [7475]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7475 or target_col == 7475). Every well: [[PRSS53 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRSS53.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
