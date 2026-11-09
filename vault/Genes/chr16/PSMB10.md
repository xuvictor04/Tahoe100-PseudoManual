---
symbol: "PSMB10"
type: "gene"
col: 12959
ensembl_id: "ENSG00000205220"
name: "proteasome 20S subunit beta 10"
location: "16q22.1"
module: 70
arm: "+"
pooled_cpm: 7.99
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 1
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 55
direction_downstream: 0
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# PSMB10

*proteasome 20S subunit beta 10* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.99× (z +5.3, q 6e-05, up in 16 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 2.30× (z +3.5, q 0.062, up in 15 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.335× (z -8.4, q 3e-14, down in 33 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMB8]] (+0.80, fdr 7e-06), [[APOL6]] (+0.79, fdr 7e-06), [[GBP4]] (+0.78, fdr 7e-06).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 55 arrows point to it, the strongest [[GBP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12959.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +5.3 | 6e-05 | 16/29 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +4.4 | 0.003 | 3/13 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.70×** | +4.1 | 0.008 | 20/34 (AsPC-1, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.30×** | +3.5 | 0.062 | 15/43 (Hs 766T, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 5 µM |  | 1.34× | +3.3 | 0.13 | 8/46 (SW480, SNU-1, …) | rises with dose | position effect removed |
| [[Omeprazole (drug)]] 0.5 µM |  | 1.48× | +3.1 | 0.19 | 11/43 (BT-474, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, none with an alert; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12959.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.335×** | -8.4 | 3e-14 | 33/45 (BT-474, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.501×** | -7.5 | 2e-11 | 31/43 (KATO III, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.387×** | -7.3 | 6e-11 | 35/47 (A498, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.389×** | -7.2 | 7e-11 | 35/46 (SW1417, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.409×** | -6.8 | 9e-10 | 29/45 (H4, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.443×** | -6.2 | 4e-08 | 30/41 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.608×** | -5.4 | 6e-06 | 31/46 (H4, BT-474, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.282×** | -5.1 | 3e-05 | 29/43 (HT-29, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.318×** | -4.6 | 3e-04 | 28/39 (SW1417, SNU-423, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.376×** | -3.9 | 0.005 | 21/43 (LoVo, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.606×** | -3.7 | 0.012 | 24/45 (MIA PaCa-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.626×** | -3.6 | 0.016 | 18/42 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.640×** | -3.4 | 0.028 | 17/47 (A498, SW 1088, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.654×** | -3.2 | 0.048 | 10/44 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.660×** | -3.2 | 0.058 | 18/44 (KATO III, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12959. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 21.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -10.4) |
| [[H4 (line)]] | wt | 10.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0345× (z -11.3) |
| [[KATO III (line)]] | alt | 12.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -11.4) |
| [[LoVo (line)]] | wt | 7.25 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0829× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 7.83 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 9.56 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -11.2) |
| [[A549 (line)]] | wt | 7.02 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0662× (z -9.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[BT-474 (line)]] | alt | 8.54 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0280× (z -13.0) |
| [[COLO 205 (line)]] | alt | 15.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0761× (z -10.7) |
| [[HT-29 (line)]] | alt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 9.09 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -10.2) |
| [[SNU-423 (line)]] | alt | 7.76 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.104× (z -8.5) |
| [[A-172 (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12959), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMB8]] | +0.80 | +0.69 / +0.79 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 999 |
| [[APOL6]] | +0.79 | +0.72 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[GBP4]] | +0.78 | +0.75 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[PSMB9]] | +0.78 | +0.74 / +0.77 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 999 |
| [[EPSTI1]] | +0.76 | +0.70 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[TAP1]] | +0.75 | +0.63 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 624 |
| [[SLC15A3]] | +0.73 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[TNFSF10]] | +0.73 | +0.74 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[TRIM22]] | +0.73 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[NMI]] | +0.73 | +0.61 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[CTSS]] | +0.72 | +0.75 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[PARP14]] | +0.72 | +0.60 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*55 arrows, 55 of them with an alert ⚠; grade A 0, B 55, C 0. Shown: the 12 strongest; 43 more arrows (43 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP1]] | B | GBP1 activity raises PSMB10's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.68× lower at baseline in the lines without GBP1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[RSAD2]] | B | RSAD2 activity raises PSMB10's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.61× lower at baseline in the lines without RSAD2 | 0.003 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[PLAAT4]] | B | PLAAT4 activity raises PSMB10's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 1.63× lower at baseline in the lines without PLAAT4 | 0.003 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[GBP4]] | B | GBP4 activity raises PSMB10's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.59× lower at baseline in the lines without GBP4 | 0.003 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[PLAAT4]] | B | PLAAT4 activity strengthens PSMB10's drug response | lines that do not express PLAAT4 (20) vs lines expressing it (27) | the lines without PLAAT4 respond 0.45× as strongly (z diff +2.19); strongest at Panobinostat 0.5 µM: 0.74x vs 0.22x (z diff +4.8) | 0.005 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1; target measured in part of the lines; artifact flags |
| [[OAS1]] | B | OAS1 activity raises PSMB10's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.50× lower at baseline in the lines without OAS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[CASP10]] | B | CASP10 activity raises PSMB10's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 1.54× lower at baseline in the lines without CASP10 | 0.010 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[CTSS]] | B | CTSS activity raises PSMB10's level | lines that do not express CTSS (15) vs lines expressing it (35) | 1.40× lower at baseline in the lines without CTSS | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[CD5L]] | B | CD5L activity raises PSMB10's level | lines that do not express CD5L (23) vs lines expressing it (27) | 1.51× lower at baseline in the lines without CD5L | 0.012 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[TRIM22]] | B | TRIM22 activity raises PSMB10's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.61× lower at baseline in the lines without TRIM22 | 0.013 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[IL15RA]] | B | IL15RA activity raises PSMB10's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 1.84× lower at baseline in the lines without IL15RA | 0.016 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |
| [[EPSTI1]] | B | EPSTI1 activity raises PSMB10's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 1.46× lower at baseline in the lines without EPSTI1 | 0.023 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.822). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.4, 51.5); signed map (62.3, 29.4). **Vector** length 79.6, 18.1% of its response variance represented; |z| ≥ 3 in 799 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.58 to 19); *Interferon gamma signaling* (reactome, mean cos +0.60 to 13); *Endosomal/Vacuolar pathway* (reactome, mean cos +0.59 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.0 | +2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +2.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.8 | +2.3 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.2 | -6.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.0 | -2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.8 | -7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -5.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.2 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -5.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 20S subunit beta 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,934,506-67,936,864 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LMP10, MGC1665, beta2i; previously MECL1 |
| Gene groups (HGNC) | Proteasome |
| Hallmark sets | ALLOGRAFT_REJECTION, XENOBIOTIC_METABOLISM, INTERFERON_GAMMA_RESPONSE |
| Reactome | 7 pathways, smallest: Antigen processing: Ub, ATP-independent proteasomal degradation; Cross-presentation of soluble exogenous antigens (endosomes); Proteasome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [P40306](https://www.uniprot.org/uniprotkb/P40306) (Proteasome subunit beta type-10):

> The proteasome is a multicatalytic proteinase complex which is characterized by its ability to cleave peptides with Arg, Phe, Tyr, Leu, and Glu adjacent to the leaving group at neutral or slightly basic pH. The proteasome has an ATP-dependent proteolytic activity. This subunit is involved in antigen processing to generate class I binding peptides.

**Summary**, from NCBI Gene [5699](https://www.ncbi.nlm.nih.gov/gene/5699):

> The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent process in a non-lysosomal pathway. An essential function of a modified proteasome, the …

**Accessions** — [HGNC:9538](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9538) · Entrez [5699](https://www.ncbi.nlm.nih.gov/gene/5699) · UniProt [P40306](https://www.uniprot.org/uniprotkb/P40306) · Ensembl [ENSG00000205220](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205220)

## Data

Gene col 12959: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12959); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12959, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12959]; `tensor/DDL_lfc|DDL_z.npy` [12959]; `embed/gene_vectors.npy` [12959]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12959 or target_col == 12959). Every well: [[PSMB10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMB10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
