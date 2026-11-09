---
symbol: "CPNE7"
type: "gene"
col: 10959
ensembl_id: "ENSG00000178773"
name: "copine 7"
location: "16q24.3"
module: 18
arm: "+"
pooled_cpm: 18.54
n_lines_expressing: 37
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# CPNE7

*copine 7* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.71× (z +11.5, q 6e-28, up in 22 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Dexamethasone (drug)]] 5 µM: 1.41× (z +4.0, q 0.005, up in 13 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 0.686× (z -6.2, q 3e-07, down in 20 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTA1]] (+0.69, fdr 7e-06), [[P2RX5]] (+0.68, fdr 7e-06), [[CAD]] (+0.67, fdr 7e-06); moves opposite to [[ATP5IF1]] (-0.57, fdr 1e-05), [[ASB8]] (-0.56, fdr 2e-05), [[SELENOK]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[BTNL9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10959.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +11.5 | 6e-28 | 22/30 (LS 180, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +10.3 | 2e-22 | 17/22 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +8.3 | 2e-14 | 19/28 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.58×** | +5.3 | 2e-05 | 19/35 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.1 | 0.004 | 15/32 (NCI-H2347, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.005 | 13/35 (hTERT-HPNE, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.41×** | +4.0 | 0.005 | 13/35 (AsPC-1, NCI-H460, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.37×** | +3.6 | 0.020 | 11/34 (AsPC-1, LOX-IMVI, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.028 | 13/35 (A-172, LoVo, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.030 | 17/35 (NCI-H1792, BT-474, …) | rises with dose | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.030 | 14/35 (hTERT-HPNE, LOX-IMVI, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.2 | 0.070 | 15/31 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.076 | 11/35 (COLO 205, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.079 | 12/35 (NCI-H1792, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.079 | 12/34 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.082 | 8/35 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.082 | 10/34 (NCI-H1792, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +3.0 | 0.085 | 9/35 (NCI-H2030, SW 900, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10959.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.686×** | -6.2 | 3e-07 | 20/35 (RKO, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.616×** | -5.6 | 5e-06 | 21/35 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.483×** | -4.4 | 0.002 | 14/32 (RKO, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.705×** | -4.1 | 0.006 | 16/35 (SNU-423, NCI-H460, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.783×** | -4.0 | 0.006 | 19/33 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.697×** | -4.0 | 0.007 | 15/34 (SNU-423, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.713×** | -3.9 | 0.007 | 17/35 (SW48, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.730×** | -3.7 | 0.017 | 11/34 (SW48, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | **0.737×** | -3.6 | 0.023 | 11/35 (RKO, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.765× | -3.1 | 0.10 | 15/35 (MIA PaCa-2, SW48, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10959. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 34.7 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 6.73× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -13.9) |
| [[MIA PaCa-2 (line)]] | alt | 66.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -9.1) |
| [[A-172 (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -9.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.206× (z -8.7) ⚠ cell-cycle shift, explains ~72% of this change |
| [[H4 (line)]] | wt | 13.1 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0690× (z -9.0) |
| [[LS 180 (line)]] | wt | 25.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.69× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 18.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +8.9) | — |
| [[RKO (line)]] | wt | 72.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -15.4) |
| [[SNU-1 (line)]] | wt | 40.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -10.6) |
| [[SW 900 (line)]] | alt | 7.76 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.106× (z -8.7) ⚠ toxic; unreliable plate only |
| [[SW48 (line)]] | wt | 63.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -10.9) |
| [[A498 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 11.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10959), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTA1]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[P2RX5]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[CAD]] | +0.67 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[SEH1L]] | +0.66 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[CLUH]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[TOP1MT]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[LETM1]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[DAZAP1]] | +0.63 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[SLC19A1]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[MRPS25]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[UBE2G2]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[PUS1]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5IF1]] | -0.57 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[ASB8]] | -0.56 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[SELENOK]] | -0.54 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[SYNRG]] | -0.53 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[SNRPB2]] | -0.53 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[PSMD10]] | -0.53 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[RNF181]] | -0.52 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[SRP14]] | -0.52 | -0.49 / -0.53 | both halves | 2e-05 |  |
| [[TCEAL8]] | -0.52 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[WDR83OS]] ⚠ | -0.50 | -0.43 / -0.51 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises CPNE7's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[BTNL9]] | C | BTNL9 activity raises CPNE7's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 2.64× lower at baseline in the lines without BTNL9 | 0.019 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BTNL9]] | C | CPNE7 activity raises BTNL9's level | lines that do not express CPNE7 (13) vs lines expressing it (37) | 2.76× lower at baseline in the lines without CPNE7 | 0.095 | ⚠ within organs, on part of the lines; also absent: BTNL9, HSBP1L1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.1, -36.1); signed map (-2.1, -54.9). **Vector** length 92.8, 23.7% of its response variance represented; |z| ≥ 3 in 790 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +11.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +5.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.2 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +3.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.6 | +1.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.6 | +1.5 |
| fall | [[NG25 (drug)]] 5 µM |  | -3.5 | -4.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.6 | -6.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.9 | -5.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.9 | -4.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -1.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.5 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | copine 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:89,575,758-89,597,246 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Copines |
| Reactome | 3 pathways, smallest: Glycerophospholipid biosynthesis; Phospholipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBL6](https://www.uniprot.org/uniprotkb/Q9UBL6) (Copine-7):

> Calcium-dependent phospholipid-binding protein that may play a role in calcium-mediated intracellular processes.

**Summary**, from NCBI Gene [27132](https://www.ncbi.nlm.nih.gov/gene/27132):

> This gene encodes a member of the copine family, which is composed of calcium-dependent membrane-binding proteins. The gene product contains two N-terminal C2 domains and one von Willebrand factor A domain. The encoded protein may be involved in membrane trafficking. Two alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2008]

**Accessions** — [HGNC:2320](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2320) · Entrez [27132](https://www.ncbi.nlm.nih.gov/gene/27132) · UniProt [Q9UBL6](https://www.uniprot.org/uniprotkb/Q9UBL6) · Ensembl [ENSG00000178773](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178773)

## Data

Gene col 10959: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10959); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10959, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10959]; `tensor/DDL_lfc|DDL_z.npy` [10959]; `embed/gene_vectors.npy` [10959]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10959 or target_col == 10959). Every well: [[CPNE7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPNE7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
