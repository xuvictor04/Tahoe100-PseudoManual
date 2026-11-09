---
symbol: "PAOX"
type: "gene"
col: 7317
ensembl_id: "ENSG00000148832"
name: "polyamine oxidase"
location: "10q26.3"
module: 20
arm: "-"
pooled_cpm: 3.17
n_lines_expressing: 45
n_dd_up: 8
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# PAOX

*polyamine oxidase* — 10q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.16× (z +8.7, q 1e-15, up in 25 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.512× (z -7.6, q 2e-11, down in 22 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAMSAP3]] (+0.59, fdr 3e-05), [[DENND6B]] (+0.59, fdr 1e-05), [[CERS4]] (+0.57, fdr 1e-05); moves opposite to [[SDHD]] (-0.56, fdr 3e-05), [[FRAS1]] (-0.55, fdr 3e-05), [[M6PR]] (-0.51, fdr 3e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7317.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.16×** | +8.7 | 1e-15 | 25/41 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.94×** | +6.8 | 2e-09 | 16/36 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.046 | 5/37 (PANC-1, A-427, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.84×** | +3.6 | 0.046 | 1/8 (SW480) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.057 | 8/39 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +3.4 | 0.057 | 7/39 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.065 | 4/30 (SNU-423, A549, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.073 | 5/35 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7317.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.512×** | -7.6 | 2e-11 | 22/41 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.588×** | -6.0 | 5e-07 | 17/26 (A549, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.596×** | -5.6 | 3e-06 | 12/22 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.648×** | -4.9 | 1e-04 | 12/41 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.636×** | -4.7 | 3e-04 | 11/36 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.663×** | -4.7 | 3e-04 | 13/36 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.671×** | -4.4 | 0.001 | 9/30 (Panc 03.27, C-33 A, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.658×** | -4.3 | 0.001 | 14/37 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.487×** | -4.3 | 0.001 | 10/36 (Hs 766T, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.696×** | -4.1 | 0.002 | 12/40 (A-427, PANC-1, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.754×** | -3.2 | 0.066 | 5/37 (NCI-H1792, RPMI-7951, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.735×** | -3.2 | 0.066 | 12/37 (LS 180, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7317. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1.98 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0728× (z -9.7) ⚠ cell-cycle shift, explains ~95% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.0934× (z -8.5) |
| [[A-172 (line)]] | wt | 8.03 | 0 | 2 (1 ⚠) | — | [[Pimozide (drug)]] 0.05 µM 0.0802× (z -12.3) |
| [[A-427 (line)]] | wt | 3.29 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0659× (z -8.9) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 4.30 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0867× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 4.55 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0669× (z -8.9) |
| [[PANC-1 (line)]] | alt | 4.73 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.138× (z -9.4) ⚠ toxic |
| [[SW1417 (line)]] | alt | 5.48 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.234 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.777 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.364 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.865 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.819 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.391 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.306 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7317), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMSAP3]] | +0.59 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[DENND6B]] | +0.59 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[CERS4]] | +0.57 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[CYS1]] | +0.57 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[BRSK1]] | +0.55 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[PGBD1]] | +0.55 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[MAP3K10]] | +0.54 | +0.39 / +0.70 | both halves | 6e-05 |  |
| [[UPK1A-AS1]] | +0.53 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[MMP17]] | +0.53 | +0.50 / +0.33 | both halves | 1e-04 |  |
| [[RNF223]] | +0.51 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[ARVCF]] | +0.50 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[LRRC8E]] | +0.49 | +0.49 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHD]] | -0.56 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[FRAS1]] | -0.55 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[M6PR]] | -0.51 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[TBC1D5]] | -0.48 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[EXOC4]] | -0.47 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[XNDC1N]] | -0.46 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[DPAGT1]] | -0.44 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[XRCC5]] | -0.43 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[SNX5]] | -0.43 | -0.21 / -0.43 | both halves | 7e-04 |  |
| [[DISC1]] | -0.43 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[KIF26B]] | -0.42 | -0.28 / -0.35 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers PAOX's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PDZD4]] | B | PDZD4 activity raises PAOX's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 1.44× lower at baseline in the lines without PDZD4 | 0.080 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.360). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.9, 27.3); signed map (0.0, 10.2). **Vector** length 42.5, 5.00% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +1.5 | +6.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.5 | +8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +1.3 | +0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +1.2 | +3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.2 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.0 | +3.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +0.8 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +0.8 | +1.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +0.7 | +2.0 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -0.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.2 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | +0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.5 | -7.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.9 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -0.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | polyamine oxidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.3 — chr10:133,379,261-133,391,694 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAO |
| Gene groups (HGNC) | Flavoproteins; Polyamine oxidases |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 8 pathways, smallest: Interconversion of polyamines; Amine Oxidase reactions; Metabolism of polyamines |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6QHF9](https://www.uniprot.org/uniprotkb/Q6QHF9) (Peroxisomal N(1)-acetyl-spermine/spermidine oxidase):

> Flavoenzyme which catalyzes the oxidation of N(1)-acetylspermine to spermidine and is thus involved in the polyamine back-conversion. Can also oxidize N(1)-acetylspermidine to putrescine. Substrate specificity: N(1)-acetylspermine = N(1)-acetylspermidine > N(1),N(12)-diacylspermine >> spermine. Does not oxidize spermidine. Plays an important role in the regulation of polyamine intracellular concentration and has the potential to act as a determinant of cellular sensitivity to the antitumor …

**Summary**, from NCBI Gene [196743](https://www.ncbi.nlm.nih.gov/gene/196743):

> Enables polyamine oxidase activity. Involved in polyamine metabolic process and positive regulation of spermidine biosynthetic process. Predicted to be located in cytosol and peroxisomal matrix. Predicted to be active in cytoplasm. Implicated in lung non-small cell carcinoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20837](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20837) · Entrez [196743](https://www.ncbi.nlm.nih.gov/gene/196743) · UniProt [Q6QHF9](https://www.uniprot.org/uniprotkb/Q6QHF9) · Ensembl [ENSG00000148832](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148832)

## Data

Gene col 7317: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7317); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7317, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7317]; `tensor/DDL_lfc|DDL_z.npy` [7317]; `embed/gene_vectors.npy` [7317]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7317 or target_col == 7317). Every well: [[PAOX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAOX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
