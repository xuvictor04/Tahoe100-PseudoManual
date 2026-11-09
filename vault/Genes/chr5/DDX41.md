---
symbol: "DDX41"
type: "gene"
col: 11386
ensembl_id: "ENSG00000183258"
name: "DEAD-box helicase 41"
location: "5q35.3"
module: 103
arm: "+"
pooled_cpm: 40.92
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# DDX41

*DEAD-box helicase 41* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.32× (z +12.3, q 4e-32, up in 46 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.16× (z +5.3, q 3e-05, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.439× (z -15.1, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPFIA4]] (+0.72, fdr 7e-06), [[AK2]] (+0.68, fdr 7e-06), [[DPYSL4]] (+0.64, fdr 7e-06); moves opposite to [[PLEKHA5]] (-0.49, fdr 8e-05), [[SH3D19]] (-0.49, fdr 4e-05), [[PTPN21]] (-0.48, fdr 3e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PCED1B]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PPFIA4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11386.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.32×** | +12.3 | 4e-32 | 46/48 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.16×** | +5.3 | 3e-05 | 28/48 (HOP62, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.25×** | +4.1 | 0.009 | 23/48 (NCI-H1573, Hs 766T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.35×** | +4.0 | 0.009 | 24/45 (A498, SW480, …) | inconsistent across doses | composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +4.0 | 0.009 | 26/48 (SW480, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.35×** | +3.7 | 0.024 | 20/48 (HEC-1-A, J82, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.33×** | +3.4 | 0.047 | 19/43 (LS 180, A498, …) | inconsistent across doses | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~20% of this change | **1.28×** | +3.2 | 0.091 | 21/47 (AsPC-1, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[venetoclax (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.091 | 15/48 (SW1417, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.28× | +3.1 | 0.11 | 17/47 (SW480, AN3 CA, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11386.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.439×** | -15.1 | 0e+00 | 43/48 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.483×** | -9.7 | 6e-20 | 37/48 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.516×** | -8.5 | 3e-15 | 34/48 (C32, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.629×** | -8.5 | 4e-15 | 43/48 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.665×** | -5.5 | 5e-06 | 31/48 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.726×** | -4.3 | 0.002 | 26/48 (SW1417, H4, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.736×** | -4.1 | 0.003 | 21/48 (C32, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.747×** | -3.8 | 0.011 | 23/47 (SK-MEL-2, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.757×** | -3.7 | 0.011 | 22/48 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.830×** | -3.5 | 0.027 | 18/48 (SNU-423, PANC-1, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.642×** | -3.1 | 0.097 | 20/48 (C32, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.847× | -3.1 | 0.099 | 15/48 (SNU-423, C32, …) | rises with dose | low cells (technical?) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **0.798×** | -3.1 | 0.099 | 11/48 (SW1417, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11386. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 153 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0890× (z -26.8) |
| [[C-33 A (line)]] | alt | 100 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -19.6) |
| [[SK-MEL-2 (line)]] | alt | 91.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -18.4) |
| [[MIA PaCa-2 (line)]] | alt | 144 | 1 (1 ⚠) | 5 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.63× (z +13.0) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -24.6) |
| [[A-172 (line)]] | wt | 55.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -13.2) |
| [[A-427 (line)]] | wt | 41.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0926× (z -18.4) |
| [[H4 (line)]] | wt | 45.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 57.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -19.6) |
| [[NCI-H2347 (line)]] | alt | 34.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -13.6) |
| [[SNU-1 (line)]] | wt | 41.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0738× (z -14.0) |
| [[SNU-423 (line)]] | alt | 62.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -22.4) |
| [[SW 1088 (line)]] | alt | 98.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0287× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 18.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -10.9) |
| [[BT-474 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -9.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 68.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -15.3) |
| [[CHP-212 (line)]] | wt | 43.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -8.7) |
| [[HOP62 (line)]] | alt | 30.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.2) |
| [[Hs 766T (line)]] | wt | 41.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -9.4) |
| [[J82 (line)]] | alt | 44.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 56.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 37.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -11.4) |
| [[PANC-1 (line)]] | alt | 28.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -14.0) |
| [[SW 900 (line)]] | alt | 99.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -11.8) |
| [[A498 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11386), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPFIA4]] | +0.72 | +0.76 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[AK2]] | +0.68 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[DPYSL4]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[PFKL]] | +0.64 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[MAPK7]] | +0.62 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[PLOD1]] | +0.62 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[ABCB6]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[GANAB]] | +0.60 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[PLXNB3]] | +0.60 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[CHSY1]] | +0.59 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[TBC1D9B]] | +0.58 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[PRSS53]] | +0.57 | +0.64 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHA5]] | -0.49 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[SH3D19]] | -0.49 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[PTPN21]] | -0.48 | -0.46 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCED1B]] | B | PCED1B activity lowers DDX41's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 1.65× higher at baseline in the lines without PCED1B | 0.057 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPFIA4]] | C | DDX41's natural level strengthens PPFIA4's drug response | DDX41's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.49; direction not clear | 0.046 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.771). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.0, -22.0); signed map (-39.8, 26.2). **Vector** length 122, 33.6% of its response variance represented; |z| ≥ 3 in 809 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *glycolysis* (hallmark, mean cos +0.59 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.6 | +5.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.0 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +2.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +4.1 | +12.3 |
|  | [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.0 | +3.0 |
|  | [[Roxadustat (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.2 | +3.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.9 | -8.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.4 | -3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.6 | -15.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.1 | -9.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.1 | -5.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.1 | -3.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.0 | -3.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -0.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 41 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:177,511,577-177,516,961 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ABS, MGC8828 |
| Gene groups (HGNC) | DEAD-box helicases; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 9 pathways, smallest: IRF3-mediated induction of type I IFN; Regulation of innate immune responses to cytosolic DNA; STING mediated induction of host immune responses |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJV9](https://www.uniprot.org/uniprotkb/Q9UJV9) (Probable ATP-dependent RNA helicase DDX41):

> Multifunctional protein that participates in many aspects of cellular RNA metabolism. Plays pivotal roles in innate immune sensing and hematopoietic homeostasis. Recognizes foreign or self-nucleic acids generated during microbial infection, thereby initiating anti-pathogen responses. Mechanistically, phosphorylation by BTK allows binding to dsDNA leading to interaction with STING1. Modulates the homeostasis of dsDNA through its ATP-dependent DNA-unwinding activity and ATP-independent …

**Summary**, from NCBI Gene [51428](https://www.ncbi.nlm.nih.gov/gene/51428):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure, such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of the DEAD box protein family are believed to be involved in embryogenesis, spermatogenesis, and cellular growth and division. …

**Accessions** — [HGNC:18674](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18674) · Entrez [51428](https://www.ncbi.nlm.nih.gov/gene/51428) · UniProt [Q9UJV9](https://www.uniprot.org/uniprotkb/Q9UJV9) · Ensembl [ENSG00000183258](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183258)

## Data

Gene col 11386: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11386); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11386, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11386]; `tensor/DDL_lfc|DDL_z.npy` [11386]; `embed/gene_vectors.npy` [11386]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11386 or target_col == 11386). Every well: [[DDX41 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX41.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
