---
symbol: "TMEM125"
type: "gene"
col: 11008
ensembl_id: "ENSG00000179178"
name: "transmembrane protein 125"
location: "1p34.2"
module: 8
arm: "+"
pooled_cpm: 2.33
n_lines_expressing: 17
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 97
direction_downstream: 135
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# TMEM125

*transmembrane protein 125* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.42× (z +10.9, q 1e-24, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM: 1.87× (z +3.8, q 0.009, up in 3 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (COLO 205 0.103×, LoVo 0.213×, HT-29 0.273×, LS 180 0.294×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (LoVo 0.132×, HT-29 0.187×, LS 180 0.227×, COLO 205 0.166×); [[Digitoxin (drug)]] 5 µM in 4 lines (LoVo 0.0682×, KATO III 0.0823×, LS 180 0.137×, NCI-H1573 0.0795×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (LS 180 0.0953×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMC4]] (+0.76, fdr 7e-06), [[TMEM45B]] (+0.74, fdr 7e-06), [[ADCY4]] (+0.74, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 97 arrows point to it, the strongest [[DCLK2]] → it (grade B ⚠); 135 go from it, the strongest it → [[FAM83E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11008.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.42×** | +10.9 | 1e-24 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.65×** | +7.8 | 1e-12 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.82×** | +7.5 | 1e-11 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.86×** | +5.9 | 7e-07 | 1/7 (NCI-H1573) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.40×** | +5.3 | 1e-05 | 2/11 (NCI-H2347, HEC-1-A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.01×** | +4.2 | 0.002 | 1/13 (COLO 205) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +4.0 | 0.005 | 0/13 | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +3.9 | 0.006 | 0/13 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.87×** | +3.8 | 0.009 | 3/13 (LoVo, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.34×** | +3.7 | 0.014 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.53×** | +3.6 | 0.014 | 4/15 (KATO III, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.024 | 0/15 | top dose only | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +3.4 | 0.024 | 4/15 (SW1417, KATO III, …) | rises with dose | position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.76×** | +3.4 | 0.024 | 0/13 | top dose only | position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | **1.74×** | +3.4 | 0.029 | 0/13 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.062 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.062 | 1/14 (CFPAC-1) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.95×** | +2.9 | 0.096 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.63×** | +2.8 | 0.100 | 0/13 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11008.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (COLO 205 0.103×, LoVo 0.213×, HT-29 0.273×, LS 180 0.294×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (LoVo 0.132×, HT-29 0.187×, LS 180 0.227×, COLO 205 0.166×); [[Digitoxin (drug)]] 5 µM in 4 lines (LoVo 0.0682×, KATO III 0.0823×, LS 180 0.137×, NCI-H1573 0.0795×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (LS 180 0.0953×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.560× | -3.6 | 0.12 | 13/14 (LS 180, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); position effect removed |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | 0.568× | -3.5 | 0.12 | 0/15 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | 0.561× | -3.4 | 0.12 | 8/15 (LS 180, KATO III, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Allopurinol (drug)]] 0.5 µM |  | 0.583× | -3.3 | 0.13 | 1/15 (NCI-H2347) | inconsistent across doses |  |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 0.706× | -3.0 | 0.28 | 5/15 (KATO III, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11008. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 18.2 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0795× (z -13.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0953× (z -12.1) |
| [[HT-29 (line)]] | alt | 13.3 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0645× (z -12.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -11.6) |
| [[LoVo (line)]] | wt | 5.73 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -12.4) |
| [[COLO 205 (line)]] | alt | 9.21 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -11.0) |
| [[KATO III (line)]] | alt | 15.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0823× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.263× (z -8.7) |
| [[HCT15 (line)]] | alt | 11.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0469× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 5.91 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0795× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 3.38 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0831× (z -9.1) |
| [[A-172 (line)]] | wt | 0.194 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.155 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.160 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.154 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.958 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.211 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.179 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.218 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.197 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.277 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.209 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.250 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.188 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.260 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.235 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.246 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.147 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.174 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.184 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.182 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.182 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.240 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.149 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.204 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.171 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.155 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.207 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.277 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.157 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.866 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11008), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMC4]] | +0.76 | +0.75 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[TMEM45B]] | +0.74 | +0.67 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[ADCY4]] | +0.74 | +0.72 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[LINC03040]] | +0.72 | +0.65 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[TJP3]] | +0.71 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[PRR15L]] | +0.71 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[ESRP1]] | +0.71 | +0.71 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[SLC44A4]] | +0.70 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[FUT3]] | +0.70 | +0.71 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[USH1C]] | +0.69 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[LINC02253]] | +0.68 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[RORC]] | +0.67 | +0.60 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*97 arrows, 97 of them with an alert ⚠; grade A 0, B 7, C 90. Shown: the 12 strongest; 85 more arrows (85 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCLK2]] | B | DCLK2 activity lowers TMEM125's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 3.38× higher at baseline in the lines without DCLK2 | 0.005 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[TTC28]] | B | TTC28 activity lowers TMEM125's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 3.88× higher at baseline in the lines without TTC28 | 0.006 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[LINC03041]] | B | LINC03041 activity lowers TMEM125's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 3.30× higher at baseline in the lines without LINC03041 | 0.017 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent |
| [[SRMS]] | B | SRMS activity raises TMEM125's level | lines that do not express SRMS (14) vs lines expressing it (36) | 1.74× lower at baseline in the lines without SRMS | 0.033 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[PLEKHG1]] | B | PLEKHG1 activity raises TMEM125's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 2.07× lower at baseline in the lines without PLEKHG1 | 0.042 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[SLC44A3]] | B | SLC44A3 activity raises TMEM125's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 2.02× lower at baseline in the lines without SLC44A3 | 0.059 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[BNC2]] | B | BNC2 activity lowers TMEM125's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 2.72× higher at baseline in the lines without BNC2 | 0.085 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[TMPRSS4]] | C | TMPRSS4 activity raises TMEM125's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 4.50× lower at baseline in the lines without TMPRSS4 | 2e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[ATP2C2]] | C | ATP2C2 activity raises TMEM125's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 4.32× lower at baseline in the lines without ATP2C2 | 4e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |
| [[RAB25]] | C | RAB25 activity raises TMEM125's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 4.49× lower at baseline in the lines without RAB25 | 4e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[MAL2]] | C | MAL2 activity raises TMEM125's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 3.95× lower at baseline in the lines without MAL2 | 8e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; co-absent with the target |
| [[ST14]] | C | ST14 activity raises TMEM125's level | lines that do not express ST14 (32) vs lines expressing it (18) | 4.29× lower at baseline in the lines without ST14 | 9e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1; co-absent with the target |

### Downstream of this gene

*135 arrows, 135 of them with an alert ⚠; grade A 0, B 46, C 89. Shown: the 12 strongest; 123 more arrows (123 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83E]] | B | TMEM125 activity raises FAM83E's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 5.18× lower at baseline in the lines without TMEM125 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[SLC44A3]] | B | TMEM125 activity raises SLC44A3's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 3.68× lower at baseline in the lines without TMEM125 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[DCLK2]] | B | TMEM125 activity lowers DCLK2's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 5.38× higher at baseline in the lines without TMEM125 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[TMEM184A]] | B | TMEM125 activity raises TMEM184A's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 3.03× lower at baseline in the lines without TMEM125 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[ARHGEF16]] | B | TMEM125 activity raises ARHGEF16's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 3.83× lower at baseline in the lines without TMEM125 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[ELMO3]] | B | TMEM125 activity raises ELMO3's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 2.87× lower at baseline in the lines without TMEM125 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[SYTL1]] | B | TMEM125 activity raises SYTL1's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 3.36× lower at baseline in the lines without TMEM125 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[TTC28]] | B | TMEM125 activity lowers TTC28's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 6.25× higher at baseline in the lines without TMEM125 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[BNC2]] | B | TMEM125 activity lowers BNC2's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 7.00× higher at baseline in the lines without TMEM125 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[OCLN]] | B | TMEM125 activity strengthens OCLN's drug response | lines that do not express TMEM125 (14) vs lines expressing it (16) | the lines without TMEM125 respond 0.17× as strongly (z diff +4.88); strongest at Homoharringtonine 5 µM: 1.12x vs 0.42x (z diff +8.2) | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; target measured in part of the lines; artifact flags |
| [[MROH7]] | B | TMEM125 activity raises MROH7's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 2.94× lower at baseline in the lines without TMEM125 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[AMN]] | B | TMEM125 activity raises AMN's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 2.30× lower at baseline in the lines without TMEM125 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.9, 54.9); signed map (58.5, 6.3). **Vector** length 51.9, 18.1% of its response variance represented; |z| ≥ 3 in 338 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +10.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.7 | +5.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +0.9 | +0.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -0.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.9 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 125 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:43,269,983-43,274,002 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC17299 |
| Matched by | ensembl_id |

UniProt [Q96AQ2](https://www.uniprot.org/uniprotkb/Q96AQ2) carries no function annotation.

**Summary**, from NCBI Gene [128218](https://www.ncbi.nlm.nih.gov/gene/128218):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28275](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28275) · Entrez [128218](https://www.ncbi.nlm.nih.gov/gene/128218) · UniProt [Q96AQ2](https://www.uniprot.org/uniprotkb/Q96AQ2) · Ensembl [ENSG00000179178](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179178)

## Data

Gene col 11008: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11008); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11008, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11008]; `tensor/DDL_lfc|DDL_z.npy` [11008]; `embed/gene_vectors.npy` [11008]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11008 or target_col == 11008). Every well: [[TMEM125 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM125.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
