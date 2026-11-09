---
symbol: "NUP37"
type: "gene"
col: 1103
ensembl_id: "ENSG00000075188"
name: "nucleoporin 37"
location: "12q23.2"
module: 22
arm: "+"
pooled_cpm: 27.92
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 3
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# NUP37

*nucleoporin 37* — 12q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.28× (z +5.5, q 2e-05, up in 19 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.736× (z -6.7, q 1e-08, down in 20 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PF-06260933 (drug)]] 5 µM: 0.660× (z -4.8, q 4e-04, down in 21 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 9 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (PANC-1 0.292×, SW480 0.434×, NCI-H460 0.360×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW48 0.104×, HEC-1-A 0.413×, NCI-H1573 0.364×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.336×, SW480 0.392×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POC5]] (+0.65, fdr 1e-05), [[NSL1]] (+0.61, fdr 1e-05), [[CEP295]] (+0.59, fdr 9e-06); moves opposite to [[EPB41L5]] (-0.47, fdr 5e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SRC]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1103.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +5.5 | 2e-05 | 19/48 (KATO III, AsPC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.27×** | +5.2 | 5e-05 | 19/47 (NCI-H1573, NCI-H1792, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.18× | +5.1 | 7e-05 | 19/48 (NCI-H2347, SW480, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.46×** | +4.3 | 0.002 | 10/46 (NCI-H1573, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.5 | 0.062 | 9/48 (AsPC-1, NCI-H1792, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | 1.16× | +3.3 | 0.098 | 17/45 (hTERT-HPNE, CHP-212, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.15× | +3.2 | 0.13 | 10/48 (HT-29, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1103.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 9 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (PANC-1 0.292×, SW480 0.434×, NCI-H460 0.360×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW48 0.104×, HEC-1-A 0.413×, NCI-H1573 0.364×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.336×, SW480 0.392×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.736×** | -6.7 | 1e-08 | 20/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.768×** | -5.5 | 8e-06 | 23/47 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.660×** | -4.8 | 4e-04 | 21/47 (SW1417, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.865× | -4.5 | 0.001 | 11/48 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.944× | -4.0 | 0.008 | 3/48 (COLO 205, RPMI-7951, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -3.5 | 0.033 | 19/48 (PANC-1, SW480, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -3.5 | 0.033 | 14/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.905× | -3.1 | 0.16 | 15/48 (SNU-1, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.870× | -3.0 | 0.16 | 14/48 (PANC-1, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1103. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 37.5 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.292× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 36.7 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.392× (z -11.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 29.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 33.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -19.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.372× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 18.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 47.3 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.131× (z -9.4) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 40.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 26.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.356× (z -8.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 37.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.387× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 29.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.360× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 29.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1103), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POC5]] | +0.65 | +0.69 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[NSL1]] | +0.61 | +0.66 / +0.57 | both halves | 1e-05 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| [[CEP295]] | +0.59 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[ARMC1]] | +0.59 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[KNSTRN]] | +0.58 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[ZMYM1]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[HYLS1]] | +0.58 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[CEP192]] | +0.57 | +0.42 / +0.62 | both halves | 4e-05 | pathway: Mitotic Prometaphase |
| [[ZNF273]] | +0.57 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[MIS18A]] | +0.57 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[CKAP2L]] | +0.55 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[DEPDC1]] | +0.55 | +0.60 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L5]] | -0.47 | -0.47 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRC]] | B | SRC activity lowers NUP37's level | compounds that target SRC: 2 of 3 raise it (NG25, Ponatinib) | 67% of the class's compounds vs 0.8% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.505). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.4, -57.3); signed map (-43.1, -33.8). **Vector** length 86.2, 17.7% of its response variance represented; |z| ≥ 3 in 692 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Activation of NIMA Kinases NEK9, NEK6, NEK7* (reactome, mean cos +0.50 to 4); *Golgi Cisternae Pericentriolar Stack Reorganization* (reactome, mean cos +0.50 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.1 | +5.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.5 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.0 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +3.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -2.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.7 | -5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.2 | -1.3 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -4.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Pentamidine (isethionate) (drug)]] 5 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | nucleoporin 37 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.2 — chr12:102,073,103-102,120,120 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC5585, FLJ22618 |
| Gene groups (HGNC) | WD repeat domain containing; Nucleoporins |
| Reactome | 85 pathways, smallest: Postmitotic nuclear pore complex (NPC) reformation; IP3 and IP4 transport between cytosol and nucleus; IP6 and IP7 transport between cytosol and nucleus |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFH4](https://www.uniprot.org/uniprotkb/Q8NFH4) (Nucleoporin Nup37):

> Component of the Nup107-160 subcomplex of the nuclear pore complex (NPC). The Nup107-160 subcomplex is required for the assembly of a functional NPC. The Nup107-160 subcomplex is also required for normal kinetochore microtubule attachment, mitotic progression and chromosome segregation.

**Summary**, from NCBI Gene [79023](https://www.ncbi.nlm.nih.gov/gene/79023):

> Nuclear pore complexes (NPCs) are used for transporting macromolecules between the cytoplasm and the nucleus. NPCs consist of multiple copies of 30 distinct proteins (nucleoporins), which assemble into biochemically-separable subcomplexes. The protein encoded by this gene is part of a subcomplex (Nup107-160) that is required for proper NPC function as well as for normal kinetochore-microtubule interaction and mitosis. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:29929](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29929) · Entrez [79023](https://www.ncbi.nlm.nih.gov/gene/79023) · UniProt [Q8NFH4](https://www.uniprot.org/uniprotkb/Q8NFH4) · Ensembl [ENSG00000075188](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075188)

## Data

Gene col 1103: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1103); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1103, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1103]; `tensor/DDL_lfc|DDL_z.npy` [1103]; `embed/gene_vectors.npy` [1103]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1103 or target_col == 1103). Every well: [[NUP37 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUP37.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
