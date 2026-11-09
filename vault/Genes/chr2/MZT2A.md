---
symbol: "MZT2A"
type: "gene"
col: 10367
ensembl_id: "ENSG00000173272"
name: "mitotic spindle organizing protein 2A"
location: "2q21.1"
module: 131
arm: "+"
pooled_cpm: 33.46
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 8
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# MZT2A

*mitotic spindle organizing protein 2A* — 2q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.75× (z +7.0, q 1e-09, up in 37 of 43 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A549 6.48×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.311× (z -13.2, q 4e-37, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MZT2B]] (+0.89, fdr 7e-06), [[NENF]] (+0.75, fdr 7e-06), [[MIR4458HG]] (+0.71, fdr 7e-06); moves opposite to [[LIN7C]] (-0.64, fdr 1e-05), [[BBS10]] (-0.63, fdr 7e-06), [[CSRP1]] (-0.62, fdr 1e-05).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[FGD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10367.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A549 6.48×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.75×** | +7.0 | 1e-09 | 37/43 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.21×** | +6.1 | 2e-07 | 26/37 (A549, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.76×** | +4.6 | 9e-04 | 31/46 (NCI-H2347, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +3.9 | 0.016 | 28/40 (KATO III, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.47× | +3.1 | 0.16 | 28/47 (AsPC-1, C32, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.49× | +3.1 | 0.16 | 25/47 (RKO, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | 1.49× | +3.1 | 0.16 | 25/47 (SW1417, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10367.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.311×** | -13.2 | 4e-37 | 44/47 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.377×** | -7.8 | 2e-12 | 42/47 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.390×** | -7.5 | 1e-11 | 45/48 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.468×** | -6.1 | 2e-07 | 42/48 (MIA PaCa-2, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.492×** | -5.7 | 2e-06 | 41/48 (HEC-1-A, BT-474, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.535×** | -4.8 | 1e-04 | 40/48 (H4, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.716×** | -3.8 | 0.013 | 32/48 (MIA PaCa-2, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.627×** | -3.7 | 0.014 | 32/48 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.654× | -3.1 | 0.11 | 26/48 (LoVo, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10367. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 42.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.166× (z -12.5) |
| [[A-172 (line)]] | wt | 51.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -14.1) |
| [[A-427 (line)]] | wt | 43.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -15.5) |
| [[A549 (line)]] | wt | 41.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.48× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -12.2) |
| [[H4 (line)]] | wt | 32.7 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0739× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 78.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -14.4) |
| [[HOP62 (line)]] | alt | 32.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -17.3) |
| [[J82 (line)]] | alt | 34.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -16.6) |
| [[LOX-IMVI (line)]] | wt | 29.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 40.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -16.9) |
| [[PANC-1 (line)]] | alt | 28.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -9.4) |
| [[SNU-423 (line)]] | alt | 16.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -9.2) |
| [[SW48 (line)]] | wt | 42.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -9.5) |
| [[SW480 (line)]] | alt | 35.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -12.5) |
| [[A498 (line)]] | wt | 48.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 16.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -11.3) |
| [[BT-474 (line)]] | alt | 27.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 38.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -8.6) |
| [[HS-578T (line)]] | alt | 18.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -8.5) |
| [[KATO III (line)]] | alt | 23.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -8.5) |
| [[LoVo (line)]] | wt | 32.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -8.5) |
| [[LS 180 (line)]] | wt | 31.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 45.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 32.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0646× (z -24.5) |
| [[NCI-H2347 (line)]] | alt | 27.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 36.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -14.8) |
| [[RKO (line)]] | wt | 36.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -13.8) |
| [[RPMI-7951 (line)]] | alt | 17.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 16.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -8.6) |
| [[SNU-1 (line)]] | wt | 33.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -9.5) |
| [[SW1417 (line)]] | alt | 33.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -10.1) |
| [[AN3 CA (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10367), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 15 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MZT2B]] | +0.89 | +0.90 / +0.89 | both halves | 7e-06 | pathway: Centrosome maturation; STRING 870 |
| [[NENF]] | +0.75 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[MIR4458HG]] | +0.71 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[NUDT2]] | +0.70 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[RPS19]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 | same gene group |
| [[RPLP2]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[HINT1]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[RPS14]] | +0.66 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[SNHG19]] | +0.65 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[SNHG25]] | +0.65 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[RPLP1]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[RPS29]] | +0.65 | +0.55 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN7C]] | -0.64 | -0.57 / -0.71 | both halves | 1e-05 |  |
| [[BBS10]] | -0.63 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[CSRP1]] | -0.62 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[YWHAZ]] | -0.61 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[HUWE1]] | -0.59 | -0.43 / -0.65 | both halves | 3e-05 | same gene group |
| [[SLC35A4]] | -0.59 | -0.68 / -0.40 | both halves | 5e-05 |  |
| [[NORAD]] | -0.59 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[FAT1]] | -0.59 | -0.49 / -0.68 | both halves | 1e-05 |  |
| [[PDAP1]] | -0.59 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[PRELID3B]] | -0.58 | -0.50 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGD1]] | B | FGD1 activity raises MZT2A's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.38× lower at baseline in the lines without FGD1 | 0.020 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises MZT2A's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises MZT2A's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ANP32B]] | C | ANP32B's natural level strengthens MZT2A's drug response | ANP32B's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.00; direction clear | 0.034 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others |
| [[RPL35]] | C | RPL35's natural level strengthens MZT2A's drug response | RPL35's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.34; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.637). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-46.1, -24.7); signed map (-36.2, 7.6). **Vector** length 66.5, 19.0% of its response variance represented; |z| ≥ 3 in 644 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Termination* (reactome, mean cos +0.54 to 20); *Peptide chain elongation* (reactome, mean cos +0.55 to 19); *PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA* (reactome, mean cos +0.55 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.8 | +2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | -0.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | -0.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.9 | +7.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.8 | -4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.8 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | mitotic spindle organizing protein 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.1 — chr2:131,464,900-131,492,743 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MOZART2A; previously FAM128A |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 9 pathways, smallest: Centrosome maturation; Recruitment of mitotic centrosome proteins and complexes; Recruitment of NuMA to mitotic centrosomes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P582](https://www.uniprot.org/uniprotkb/Q6P582) (Mitotic-spindle organizing protein 2A):

> Required for the recruitment and the assembly of the gamma-tubulin ring complex (gTuRC) at the centrosome. The gTuRC regulates the minus-end nucleation of alpha-beta tubulin heterodimers that grow into microtubule protafilaments, a critical step in centrosome duplication and spindle formation.

**Summary**, from NCBI Gene [653784](https://www.ncbi.nlm.nih.gov/gene/653784):

> Predicted to be involved in microtubule nucleation. Located in centrosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:33187](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33187) · Entrez [653784](https://www.ncbi.nlm.nih.gov/gene/653784) · UniProt [Q6P582](https://www.uniprot.org/uniprotkb/Q6P582) · Ensembl [ENSG00000173272](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173272)

## Data

Gene col 10367: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10367); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10367, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10367]; `tensor/DDL_lfc|DDL_z.npy` [10367]; `embed/gene_vectors.npy` [10367]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10367 or target_col == 10367). Every well: [[MZT2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MZT2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
