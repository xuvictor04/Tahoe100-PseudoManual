---
symbol: "HAUS5"
type: "gene"
col: 14589
ensembl_id: "ENSG00000249115"
name: "HAUS augmin like complex subunit 5"
location: "19q13.12"
module: 6
arm: "+"
pooled_cpm: 9.64
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# HAUS5

*HAUS augmin like complex subunit 5* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.34× (z +12.7, q 4e-34, up in 16 of 17 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.33× (z +4.2, q 0.001, up in 13 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.725× (z -7.1, q 6e-10, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCAPH2]] (+0.78, fdr 7e-06), [[MCM2]] (+0.76, fdr 7e-06), [[RFC5]] (+0.73, fdr 7e-06); moves opposite to [[NACA4P]] (-0.55, fdr 1e-05, ⚠ NACA4P in the vector space only through flagged drug-doses).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 13 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14589.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.34×** | +12.7 | 4e-34 | 16/17 (HEC-1-A, H4, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.00×** | +10.7 | 2e-24 | 25/32 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.78×** | +9.0 | 6e-17 | 28/47 (PANC-1, LoVo, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.81×** | +8.5 | 3e-15 | 18/27 (LOX-IMVI, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.65×** | +7.4 | 1e-11 | 21/38 (SW480, HT-29, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.59×** | +7.2 | 5e-11 | 20/47 (LoVo, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.58×** | +7.1 | 1e-10 | 23/47 (PANC-1, LoVo, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.35×** | +4.7 | 2e-04 | 16/47 (PANC-1, A-427, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.001 | 13/46 (NCI-H460, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.30×** | +3.9 | 0.004 | 5/46 (PANC-1, A-427, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.19× | +3.8 | 0.007 | 6/47 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.29×** | +3.8 | 0.007 | 10/44 (PANC-1, A-427, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.22×** | +3.0 | 0.099 | 6/43 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 1.15× | +3.0 | 0.099 | 5/46 (LOX-IMVI, A-427, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.22× | +3.0 | 0.10 | 10/39 (C32, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14589.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.725×** | -7.1 | 6e-10 | 26/48 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.657×** | -6.5 | 2e-08 | 21/45 (H4, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.685×** | -5.9 | 6e-07 | 17/46 (HEC-1-A, SW480, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.601×** | -4.2 | 0.005 | 10/41 (CFPAC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.05 µM |  | **0.798×** | -3.3 | 0.095 | 12/44 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | 0.815× | -3.1 | 0.20 | 8/46 (NCI-H2030, NCI-H661, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14589. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 8.97 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0335× (z -13.7) |
| [[Hs 766T (line)]] | wt | 6.40 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.108× (z -8.8) |
| [[A-172 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14589), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCAPH2]] | +0.78 | +0.72 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[MCM2]] | +0.76 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[RFC5]] | +0.73 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[FANCG]] | +0.73 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[POLD3]] | +0.69 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[TONSL]] | +0.69 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[RNASEH2A]] | +0.68 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[ZWINT]] | +0.68 | +0.71 / +0.65 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[LIG1]] | +0.68 | +0.57 / +0.70 | both halves | 8e-06 |  |
| [[MCM5]] | +0.68 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[WDHD1]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[GINS1]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NACA4P]] ⚠ | -0.55 | -0.54 / -0.54 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises HAUS5's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.82× lower at baseline in the lines without TCF19 | 0.027 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises HAUS5's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.64× lower at baseline in the lines without E2F8 | 0.086 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[ZNF66]] | B | ZNF66 activity raises HAUS5's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 1.21× lower at baseline in the lines without ZNF66 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[HDAC6]] | B | HDAC6 activity lowers HAUS5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TK1]] | C | TK1 activity raises HAUS5's level | lines that do not express TK1 (3) vs lines expressing it (47) | 2.34× lower at baseline in the lines without TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[MYBL2]] | C | MYBL2 activity raises HAUS5's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.25× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[MCM10]] | C | MCM10 activity raises HAUS5's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 1.68× lower at baseline in the lines without MCM10 | 0.069 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.671). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.5, -42.7); signed map (-36.1, -46.5). **Vector** length 72.2, 12.2% of its response variance represented; |z| ≥ 3 in 842 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.53 to 65); *DNA strand elongation* (reactome, mean cos +0.57 to 28); *DNA Replication* (reactome, mean cos +0.54 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +5.1 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +4.9 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +4.0 | +8.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +3.2 | +4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | +2.9 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +0.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.7 | +2.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.5 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.3 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -7.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.7 | -6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +1.0 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -4.2 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | HAUS augmin like complex subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:35,612,735-35,625,355 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dgt5; previously KIAA0841 |
| Gene groups (HGNC) | HAUS augmin like complex |
| Reactome | 17 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [O94927](https://www.uniprot.org/uniprotkb/O94927) (HAUS augmin-like complex subunit 5):

> Contributes to mitotic spindle assembly, maintenance of centrosome integrity and completion of cytokinesis as part of the HAUS augmin-like complex.

**Summary**, from NCBI Gene [23354](https://www.ncbi.nlm.nih.gov/gene/23354):

> HAUS5 is 1 of 8 subunits of the 390-kD human augmin complex, or HAUS complex. The augmin complex was first identified in Drosophila, and its name comes from the Latin verb 'augmentare,' meaning 'to increase.' The augmin complex is a microtubule-binding complex involved in microtubule generation within the mitotic spindle and is vital to mitotic spindle assembly (Goshima et al., 2008 [PubMed 18443220]; Uehara et al., 2009 [PubMed 19369198]).[supplied by OMIM, Jun 2010]

**Accessions** — [HGNC:29130](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29130) · Entrez [23354](https://www.ncbi.nlm.nih.gov/gene/23354) · UniProt [O94927](https://www.uniprot.org/uniprotkb/O94927) · Ensembl [ENSG00000249115](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249115)

## Data

Gene col 14589: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14589); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14589, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14589]; `tensor/DDL_lfc|DDL_z.npy` [14589]; `embed/gene_vectors.npy` [14589]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14589 or target_col == 14589). Every well: [[HAUS5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAUS5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
